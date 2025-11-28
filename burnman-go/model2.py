import numpy as np
import matplotlib.pyplot as plt
import functions
import functions
import params

M_min, g_min, p_min, r_min, rho_min = functions.create_arrays()
M_mean, g_mean, p_mean, r_mean, rho_mean = functions.create_arrays()
M_max, g_max, p_max, r_max, rho_max = functions.create_arrays()
T_min = functions.create_temp_array('min', r_min)
T_mean = functions.create_temp_array('mean', r_mean)
T_max = functions.create_temp_array('max', r_max)

M_min, g_min, p_min, r_min, rho_min, T_min, core_boundary_min, mantle_boundary_min, inertia_min, simcount_min, core_mantle_boundary_gravity_min, mantle_shell_boundary_gravity_min, core_mantle_boundary_temp_min, mantle_shell_boundary_temp_min, core_mantle_boundary_pressure_min, mantle_shell_boundary_pressure_min = functions.iterate(M_min, g_min, p_min, r_min, rho_min, T_min)
print('\n---SIMULATION COMPLETE - MIN TEMP---')
print("Total mass: ", M_min[-1], " kg")
print("Mass deviation: ", (M_min[-1]-params.M_observed)/params.M_observed*100, "percent of observed mass")
print("Center pressure: ", p_min[0]/1000000000, " GPa")
#print("Core-mantle boundary pressure: ", core_mantle_boundary_pressure_min/1000000000, " GPa")
#print("Mantle-shell boundary pressure: ", mantle_shell_boundary_pressure_min/1000000000, " GPa")
#print("Core-mantle boundary temperature: ", core_mantle_boundary_temp_min, " [K]")
#print("Mantle-shell boundary temperature: ", mantle_shell_boundary_temp_min, " [K]")
#print("Core-mantle boundary gravity: ", core_mantle_boundary_gravity_min, " [m/s^2]")
#print("Mantle-shell boundary gravity: ", mantle_shell_boundary_gravity_min, " [m/s^2]")
print("Gravitational acceleration at surface: ", g_min[-1], " m/s^2")
print("Core radius: ", core_boundary_min/1000, " km")
print("Crust thickness: ", (params.rtotal-mantle_boundary_min)/1000, " km")
print("Moment of inertia: ", inertia_min)
print("Moment of inertia deviation: ", abs((inertia_min-params.inertia_observed)/params.inertia_observed*100))
print("Number of simulations ran: ", simcount_min)

M_mean, g_mean, p_mean, r_mean, rho_mean, T_mean, core_boundary_mean, mantle_boundary_mean, inertia_mean, simcount_mean, core_mantle_boundary_gravity_mean, mantle_shell_boundary_gravity_mean, core_mantle_boundary_temp_mean, mantle_shell_boundary_temp_mean, core_mantle_boundary_pressure_mean, mantle_shell_boundary_pressure_mean = functions.iterate(M_mean, g_mean, p_mean, r_mean, rho_mean, T_mean)
print('\n---SIMULATION COMPLETE - MEAN TEMP---')
print("Total mass: ", M_mean[-1], " kg")
print("Mass deviation: ", (M_mean[-1]-params.M_observed)/params.M_observed*100, "percent of observed mass")
print("Center pressure: ", p_mean[0]/1000000000, " GPa")
#print("Core-mantle boundary pressure: ", core_mantle_boundary_pressure_mean/1000000000, " GPa")
#print("Mantle-shell boundary pressure: ", mantle_shell_boundary_pressure_mean/1000000000, " GPa")
#print("Core-mantle boundary temperature: ", core_mantle_boundary_temp_mean, " [K]")
#print("Mantle-shell boundary pressure: ", mantle_shell_boundary_temp_mean, " [K]")
#print("Core-mantle boundary gravity: ", core_mantle_boundary_gravity_mean, " [m/s^2]")
#print("Mantle-shell boundary gravity: ", mantle_shell_boundary_gravity_mean, " [m/s^2]")
print("Gravitational acceleration at surface: ", g_mean[-1], " m/s^2")
print("Core radius: ", core_boundary_mean/1000, " km")
print("Crust thickness: ", (params.rtotal-mantle_boundary_mean)/1000, " km")
print("Moment of inertia: ", inertia_mean)
print("Moment of inertia deviation: ", abs((inertia_mean-params.inertia_observed)/params.inertia_observed*100))
print("Number of simulations ran: ", simcount_mean)

M_max, g_max, p_max, r_max, rho_max, T_max, core_boundary_max, mantle_boundary_max, inertia_max, simcount_max, core_mantle_boundary_gravity_max, mantle_shell_boundary_gravity_max, core_mantle_boundary_temp_max, mantle_shell_boundary_temp_max, core_mantle_boundary_pressure_max, mantle_shell_boundary_pressure_max = functions.iterate(M_max, g_max, p_max, r_max, rho_max, T_max)
print('\n---SIMULATION COMPLETE - MAX TEMP---')
print("Total mass: ", M_max[-1], " kg")
print("Mass deviation: ", (M_max[-1]-params.M_observed)/params.M_observed*100, "percent of observed mass")
print("Center pressure: ", p_max[0]/1000000000, " GPa")
#print("Core-mantle boundary pressure: ", core_mantle_boundary_pressure_max/1000000000, " GPa")
#print("Mantle-shell boundary pressure: ", mantle_shell_boundary_pressure_max/1000000000, " GPa")
#print("Core-mantle boundary temperature: ", core_mantle_boundary_temp_max, " [K]")
#print("Mantle-shell boundary pressure: ", mantle_shell_boundary_temp_max, " [K]")
#print("Core-mantle boundary gravity: ", core_mantle_boundary_gravity_max, " [m/s^2]")
#print("Mantle-shell boundary gravity: ", mantle_shell_boundary_gravity_max, " [m/s^2]")
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

