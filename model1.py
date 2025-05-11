import numpy as np
import matplotlib.pyplot as plt
import functions
import params

M, g, p, r, rho = functions.create_arrays()

core_boundary = params.core_boundary
mantle_boundary = params.mantle_boundary
simcount = 0
inertia = 0.0
while abs((inertia-params.inertia_observed)/params.inertia_observed*100) > 1.0 or abs((M[-1]-params.M_observed)/params.M_observed*100) > 1.0:
    simcount += 1
    print("Starting simulation ", simcount)
    for i in range(len(r)):
        if r[i] <= core_boundary:
            rho[i] = 5500.0
        elif core_boundary < r[i] and r[i] <= mantle_boundary:
            rho[i] = 3300.0
        else:
            rho[i] = 1000.0

    for i in range(0, len(r)-1):
        M[i+1] = functions.Mass(M[i], r[i+1], rho[i+1])

    for i in range(len(r)):
        g[i] = functions.Gravity(params.G, M[i], r[i])

    for i in np.flip(range(1, len(r))):
        p[i-1] = functions.Pressure(p[i], rho[i], g[i])
    
    
    inertia = functions.inertia(r, rho, params.delta_r, M)
    print('Residual moment of inertia: ', abs((inertia-params.inertia_observed)/params.inertia_observed*100), ' percent')
    print('Residual mass: ', abs((M[-1]-params.M_observed)/params.M_observed*100), ' percent')

    '''
    if inertia > inertia_observed:
        mantle_boundary += delta_r
    elif inertia < inertia_observed:
        mantle_boundary -= delta_r
    
    '''
    if M[-1] > params.M_observed:
        core_boundary -= params.delta_r
    elif M[-1] < params.M_observed:
        core_boundary += params.delta_r
    if inertia > params.inertia_observed:
        mantle_boundary -= params.delta_r
    elif inertia < params.inertia_observed:
        mantle_boundary += params.delta_r
   
fig, axs = plt.subplots(1, 4, sharey=True, layout='constrained')

ax = axs[0]
ax.plot(p/1000000000,r/1000)
ax.set_xlabel('Pressure [GPa]')
ax.set_ylabel('Radius [m]')

ax = axs[1]
ax.plot(M/10000000000000000000,r/1000)
ax.set_xlabel('Mass [1000 kg]')

ax = axs[2]
ax.plot(rho, r/1000)
ax.set_xlabel('Density [kg/m^3]')

ax = axs[3]
ax.plot(g,r/1000)
ax.set_xlabel('Gravity [m/s^2]')

plt.show()
plt.clf()

print('\n---SIMULATION COMPLETE---')
print("Total mass: ", M[-1], " kg")
print("Mass deviation: ", (M[-1]-params.M_observed)/params.M_observed*100, "percent of observed mass")
print("Center pressure: ", p[0]/1000000000, " GPa")
print("Gravitational acceleration at surface: ", g[-1], " m/s^2")
for i in range(len(r)):
    if r[i] <= core_boundary and r[i+1] > core_boundary: 
        print("Gravitational acceleration at core-mantle boundary: ", g[i], " m/s^2")
    elif r[i] <= mantle_boundary and r[i+1] > mantle_boundary:
        print("Gravitational acceleration at mantle-shell boundary: ", g[i], " m/s^2")
print("Core radius: ", core_boundary/1000, " km")
print("Crust thickness: ", (params.rtotal-mantle_boundary)/1000, " km")
print("Moment of inertia: ", inertia)
print("Number of simulations ran: ", simcount)
