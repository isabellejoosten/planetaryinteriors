import numpy as np
import matplotlib.pyplot as plt
import functions
import functions
import params

M, g, p, r, rho = functions.create_arrays()
T_min = functions.create_temp_array('min', r)
T_mean = functions.create_temp_array('mean', r)
T_max = functions.create_temp_array('max', r)

M_min, g_min, p_min, r_min, rho_min, T_min, core_boundary_min, mantle_boundary_min, inertia_min, simcount_min = functions.iterate(M, g, p, r, rho, T_min)
print('\n---SIMULATION COMPLETE - MIN TEMP---')
print("Total mass: ", M_min[-1], " kg")
print("Mass deviation: ", (M_min[-1]-params.M_observed)/params.M_observed*100, "percent of observed mass")
print("Center pressure: ", p_min[0]/1000000000, " GPa")
print("Gravitational acceleration at surface: ", g_min[-1], " m/s^2")
print("Core radius: ", core_boundary_min/1000, " km")
print("Crust thickness: ", (params.rtotal-mantle_boundary_min)/1000, " km")
print("Moment of inertia: ", inertia_min)
print("Moment of inertia deviation: ", abs((inertia_min-params.inertia_observed)/params.inertia_observed*100))
print("Number of simulations ran: ", simcount_min)

M_mean, g_mean, p_mean, r_mean, rho_mean, T_mean, core_boundary_mean, mantle_boundary_mean, inertia_mean, simcount_mean = functions.iterate(M, g, p, r, rho, T_mean)
print('\n---SIMULATION COMPLETE - MEAN TEMP---')
print("Total mass: ", M_mean[-1], " kg")
print("Mass deviation: ", (M_mean[-1]-params.M_observed)/params.M_observed*100, "percent of observed mass")
print("Center pressure: ", p_mean[0]/1000000000, " GPa")
print("Gravitational acceleration at surface: ", g_mean[-1], " m/s^2")
print("Core radius: ", core_boundary_mean/1000, " km")
print("Crust thickness: ", (params.rtotal-mantle_boundary_mean)/1000, " km")
print("Moment of inertia: ", inertia_mean)
print("Moment of inertia deviation: ", abs((inertia_mean-params.inertia_observed)/params.inertia_observed*100))
print("Number of simulations ran: ", simcount_mean)

M_max, g_max, p_max, r_max, rho_max, T_max, core_boundary_max, mantle_boundary_max, inertia_max, simcount_max = functions.iterate(M, g, p, r, rho, T_max)
print('\n---SIMULATION COMPLETE - MAX TEMP---')
print("Total mass: ", M_max[-1], " kg")
print("Mass deviation: ", (M_max[-1]-params.M_observed)/params.M_observed*100, "percent of observed mass")
print("Center pressure: ", p_max[0]/1000000000, " GPa")
print("Gravitational acceleration at surface: ", g_max[-1], " m/s^2")
print("Core radius: ", core_boundary_max/1000, " km")
print("Crust thickness: ", (params.rtotal-mantle_boundary_max)/1000, " km")
print("Moment of inertia: ", inertia_max)
print("Moment of inertia deviation: ", abs((inertia_max-params.inertia_observed)/params.inertia_observed*100))
print("Number of simulations ran: ", simcount_max)

fig, axs = plt.subplots(1, 5, sharey=True, layout='constrained')   
ax = axs[0]
ax.plot(p_min/1000000000,r_min/1000)
ax.plot(p_mean/1000000000,r_mean/1000)
ax.plot(p_max/1000000000,r_max/1000)
ax.set_xlabel('Pressure [GPa]')
ax.set_ylabel('Radius [m]')

ax = axs[1]
ax.plot(M_min/10000000000000000000,r_min/1000)
ax.plot(M_mean/10000000000000000000,r_mean/1000)
ax.plot(M_max/10000000000000000000,r_max/1000)
ax.set_xlabel('Mass [1000 kg]')

ax = axs[2]
ax.plot(rho_min, r_min/1000)
ax.plot(rho_mean, r_mean/1000)
ax.plot(rho_max, r_max/1000)
ax.set_xlabel('Density [kg/m^3]')

ax = axs[3]
ax.plot(g_min,r_min/1000)
ax.plot(g_mean,r_mean/1000)
ax.plot(g_max,r_max/1000)
ax.set_xlabel('Gravity [m/s^2]')

ax = axs[4]
ax.plot(T_min,r_min/1000)
ax.plot(T_mean,r_mean/1000)
ax.plot(T_max,r_max/1000)
ax.set_xlabel('Temperature [K]')

plt.show()
plt.clf()

