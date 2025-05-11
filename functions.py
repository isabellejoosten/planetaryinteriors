import params
import numpy as np
import matplotlib.pyplot as plt
import functions

def Pressure(p, rho, g):
    func = -rho*g
    p = p - func*params.delta_r
    return p

def Mass(M, r, rho):
    func = 4*np.pi*rho*r**2
    M += func*params.delta_r
    return M

def Gravity(G, M, r):
    if r == 0:
        g = 0
    else:
        g = G*M/r**2
    return g

def inertia(r, rho, delta_r, M):
    inertia = 0
    for i in range(len(r)):
        inertia += delta_r*rho[i]*r[i]**4

    return inertia*(8*np.pi)/(3*M[-1]*r[-1]*r[-1])

def set_density(rho, T, rho0, alpha, K, p):
    for i in range(len(T)):
        rho[i] = rho0*(1-alpha*(T[0]-T[i])+(p[0]-p[i])/K)
    return rho

def get_rayleigh(rho, alpha, g, T, D, kappa, eta):
    Ra = np.zeros(len(T))
    for i in range(len(T)):
        Ra[i] = (rho[i]*alpha*g[i]*(T[0]-T[i])*D**3)/(kappa*eta)

    return Ra

def create_arrays():
    r = np.arange(0, params.rtotal + params.delta_r, params.delta_r)
    rho = np.zeros(len(r))
    for i in range(len(r)):
        if r[i] <= params.core_boundary:
            rho[i] = 5500.0
        elif params.core_boundary < r[i] and r[i] <= params.mantle_boundary:
            rho[i] = 3300.0
        else:
            rho[i] = 1000.0
    M = np.zeros(len(r))
    p = np.zeros(len(r))
    g = np.zeros(len(r))

    return M, g, p, r, rho

def create_temp_array(Ttype, r):
    if Ttype == 'min':
        T = np.flip(np.arange(params.surface_temp, params.core_temp_min, (params.core_temp_min-params.surface_temp)/len(r)))
    elif Ttype == 'mean':
        T = np.flip(np.arange(params.surface_temp, params.core_temp_mean, (params.core_temp_mean-params.surface_temp)/len(r)))
    elif Ttype == 'max':
        T = np.flip(np.arange(params.surface_temp, params.core_temp_max-1, (params.core_temp_max-params.surface_temp)/len(r)))
    return T

def iterate(M, g, p, r, rho, T):
    inertia = 0.0
    simcount = 0
    core_boundary = params.core_boundary
    mantle_boundary = params.mantle_boundary
    while abs((inertia-params.inertia_observed)/params.inertia_observed*100) > 1.0 or abs((M[-1]-params.M_observed)/params.M_observed*100) > 1.0:
        simcount += 1
        #print("Starting simulation ", simcount)

        for i in range(0, len(r)-1):
            M[i+1] = Mass(M[i], r[i+1], rho[i+1])

        for i in range(len(r)):
            g[i] = Gravity(params.G, M[i], r[i])

        for i in np.flip(range(1, len(r))):
            p[i-1] = Pressure(p[i], rho[i], g[i])
    
        core_mantle_boundary_temp = 0
        mantle_shell_boundary_temp = 0
        core_mantle_boundary_pressure = 0
        mantle_shell_boundary_pressure = 0

        inertia = functions.inertia(r, rho, params.delta_r, M)
        for i in range(len(r)):
            if r[i] <= core_boundary:
                rho[i] = 5500.0*(1-params.core_alpha*(abs(T[0]-T[i]))+(abs(p[0]-p[i]))/params.core_K)
                if r[i] <= core_boundary and r[i+1] > core_boundary:
                    core_mantle_boundary_temp = T[i]
                    core_mantle_boundary_pressure = p[i]
            elif core_boundary < r[i] and r[i] <= mantle_boundary:
                rho[i] = 3300.0*(1-params.mantle_alpha*(abs(core_mantle_boundary_temp-T[i]))+(abs(core_mantle_boundary_pressure-p[i]))/params.mantle_K)
                if r[i] <= mantle_boundary and r[i+1] > mantle_boundary:
                    mantle_shell_boundary_temp = T[i]
                    mantle_shell_boundary_pressure = p[i]
            else:
                rho[i] = 1000.0*(1-params.shell_alpha*(abs(mantle_shell_boundary_temp-T[i]))+((mantle_shell_boundary_pressure-p[i]))/params.shell_K)

        #print('Residual moment of inertia: ', abs((inertia-params.inertia_observed)/params.inertia_observed*100), ' percent')
        #print('Residual mass: ', abs((M[-1]-params.M_observed)/params.M_observed*100), ' percent')


        if M[-1] > params.M_observed:
            core_boundary -= params.delta_r
        elif M[-1] < params.M_observed:
            core_boundary += params.delta_r
        if inertia > params.inertia_observed:
            mantle_boundary -= params.delta_r
        elif inertia < params.inertia_observed:
            mantle_boundary += params.delta_r
    
    return M, g, p, r, rho, T, core_boundary, mantle_boundary, inertia, simcount