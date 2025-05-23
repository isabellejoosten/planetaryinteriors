import numpy as np
import matplotlib.pyplot as plt
import functions

simcount = 0
rtotal = 6378.0*10**3                 # radius in [m]
delta_r = 500.0                    # step size in [m]
M_observed = 59742.0*10**20           # mass of Europa in [kg]
inertia_observed = 0.331            # observed moment of inertia taken from the planetary database
G = 6.67430*10**(-11)               # gravitational constant

core_boundary = 3450.0*10**3           # initial core radius in [m]
mantle_boundary = 6320.0*10**3        # initial distance from center to mantle-crust boundary in [m]

r = np.arange(0, rtotal + delta_r, delta_r)
rho = np.zeros(len(r))

M = np.zeros(len(r))
p = np.zeros(len(r))
g = np.zeros(len(r))

inertia = 0.0
while abs((inertia-inertia_observed)/inertia_observed*100) > 1.0 or abs((M[-1]-M_observed)/M_observed*100) > 1.0:
    simcount += 1
    print("Starting simulation ", simcount)
    for i in range(len(r)):
        if r[i] <= core_boundary:
            rho[i] = 11500.0
        elif core_boundary < r[i] and r[i] <= mantle_boundary:
            rho[i] = 4500.0
        else:
            rho[i] = 2600.0

    for i in range(0, len(r)-1):
        M[i+1] = functions.Mass(M[i], r[i+1], delta_r, rho[i+1])

    for i in range(len(r)):
        g[i] = functions.Gravity(G, M[i], r[i])

    for i in np.flip(range(1, len(r))):
        p[i-1] = functions.Pressure(p[i], rho[i], g[i], delta_r)
    
    
    inertia = functions.inertia(r, rho, delta_r, M)
    print('Residual moment of inertia: ', abs((inertia-inertia_observed)/inertia_observed*100), ' percent')
    print('Residual mass: ', abs((M[-1]-M_observed)/M_observed*100), ' percent')

    '''
    if inertia > inertia_observed:
        mantle_boundary += delta_r
    elif inertia < inertia_observed:
        mantle_boundary -= delta_r
    
    '''
    if M[-1] > M_observed:
        core_boundary -= delta_r
    elif M[-1] < M_observed:
        core_boundary += delta_r
    if inertia > inertia_observed:
        mantle_boundary -= delta_r
    elif inertia < inertia_observed:
        mantle_boundary += delta_r
    

"""
plt.plot(p,r)
plt.show()
plt.plot(M,r)
plt.show()
plt.plot(rho, r)
plt.show()
"""

print('\n---SIMULATION COMPLETE---')
print("Total mass: ", M[-1], " kg")
print("Mass deviation: ", (M[-1]-M_observed)/M_observed*100, "percent of observed mass")
print("Center pressure: ", p[0]/1000000000, " GPa")
print("Gravitational acceleration at surface: ", g[-1], " m/s^2")
print("Core radius: ", core_boundary/1000, " km")
print("Crust thickness: ", (rtotal-mantle_boundary)/1000, " km")
print("Moment of inertia: ", inertia)
print("Number of simulations ran: ", simcount)
