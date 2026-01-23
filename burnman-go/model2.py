import numpy as np
import matplotlib.pyplot as plt
import functions
import functions
import params

M_min, g_min, p_min, r_min, rho_min = functions.create_arrays(params.rtotal)
for i in range(len(r_min)):
        if r_min[i] <= params.core_boundary:
            rho_min[i] = params.density_core_Fe
        elif params.core_boundary < r_min[i] and r_min[i] <= params.mantle_boundary:
            rho_min[i] = params.density_mantle
        else:
            rho_min[i] = params.density_shell
M_mean, g_mean, p_mean, r_mean, rho_mean = functions.create_arrays(params.rtotal)
for i in range(len(r_mean)):
        if r_mean[i] <= params.core_boundary:
            rho_mean[i] = params.density_core_Fe
        elif params.core_boundary < r_mean[i] and r_mean[i] <= params.mantle_boundary:
            rho_mean[i] = params.density_mantle
        else:
            rho_mean[i] = params.density_shell
M_max, g_max, p_max, r_max, rho_max = functions.create_arrays(params.rtotal)
for i in range(len(r_max)):
        if r_max[i] <= params.core_boundary:
            rho_max[i] = params.density_core_Fe
        elif params.core_boundary < r_max[i] and r_max[i] <= params.mantle_boundary:
            rho_max[i] = params.density_mantle
        else:
            rho_max[i] = params.density_shell
T_min = functions.create_temp_array('min', r_min)
T_mean = functions.create_temp_array('mean', r_mean)
T_max = functions.create_temp_array('max', r_max)

M_min, g_min, p_min, r_min, rho_min, T_min, core_boundary_min, mantle_boundary_min, inertia_min, simcount_min, meanDensity_min, core_mantle_boundary_temp_min, core_mantle_boundary_pressure_min, core_mantle_boundary_gravity_min, mantle_shell_boundary_temp_min, mantle_shell_boundary_pressure_min, mantle_shell_boundary_gravity_min = functions.iterate(M_min, g_min, p_min, r_min, rho_min, T_min)

# Print final results
print('\n---SIMULATION COMPLETE - MIN TEMP---')
print(f"Number of iterations: {simcount_min}")

print("\n--- COMPARISON TO OBSERVED VALUES ---")
print(f"Total mass: {M_min[-1]:.3e} kg")
print(f"Observed mass: {params.M_observed} plus/minus {params.M_uncertainty} kg")
print(f"Mass deviation from observed value: {abs(M_min[-1] - params.M_observed):.3e} kg, {round(abs(M_min[-1] - params.M_observed)/params.M_uncertainty, 3)} times the uncertainty.")

print(f"\nMoment of inertia factor: {round(inertia_min, 3)}")
print(f"Observed moment of inertia factor: {params.inertia_observed} plus/minus {params.inertia_uncertainty}")
print(f"Moment of inertia factor deviation from observed value: {round(abs(inertia_min - params.inertia_observed), 4)}, {round(abs(inertia_min - params.inertia_observed)/params.inertia_uncertainty, 4)} times the uncertainty.")

print(f"\nMean density: {round(meanDensity_min, 1)} kg/m^3")
print(f"Observed mean density: {params.meanDensity_observed} plus/minus {params.meanDensity_uncertainty} kg/m^3")
print(f"Mean density deviation from observed value: {round(abs(meanDensity_min - params.meanDensity_observed), 1)} kg/m^3, {round(abs(meanDensity_min - params.meanDensity_observed)/params.meanDensity_uncertainty, 3)} times the uncertainty.")

print("\n--- CALCULATED VALUES ---")
print("Center pressure: ", p_min[0]/1000000000, " GPa")
print("Gravitational acceleration at surface: ", g_min[-1], " m/s^2")

print("\n--- INTERNAL COMPOSITION ---")
print("Core radius: ", core_boundary_min/1000, " km")
print("Mantle thickness: ", (mantle_boundary_min - core_boundary_min)/1000, " km")
print("Crust thickness: ", (params.rtotal-mantle_boundary_min)/1000, " km")

M_mean, g_mean, p_mean, r_mean, rho_mean, T_mean, core_boundary_mean, mantle_boundary_mean, inertia_mean, simcount_mean, meanDensity_mean, core_mantle_boundary_temp_mean, core_mantle_boundary_pressure_mean, core_mantle_boundary_gravity_mean, mantle_shell_boundary_temp_mean, mantle_shell_boundary_pressure_mean, mantle_shell_boundary_gravity_mean = functions.iterate(M_mean, g_mean, p_mean, r_mean, rho_mean, T_mean)


# Print final results
print('\n---SIMULATION COMPLETE - MEAN TEMP---')
print(f"Number of iterations: {simcount_mean}")

print("\n--- COMPARISON TO OBSERVED VALUES ---")
print(f"Total mass: {M_mean[-1]:.3e} kg")
print(f"Observed mass: {params.M_observed} plus/minus {params.M_uncertainty} kg")
print(f"Mass deviation from observed value: {abs(M_mean[-1] - params.M_observed):.3e} kg, {round(abs(M_mean[-1] - params.M_observed)/params.M_uncertainty, 3)} times the uncertainty.")

print(f"\nMoment of inertia factor: {round(inertia_mean, 3)}")
print(f"Observed moment of inertia factor: {params.inertia_observed} plus/minus {params.inertia_uncertainty}")
print(f"Moment of inertia factor deviation from observed value: {round(abs(inertia_mean - params.inertia_observed), 4)}, {round(abs(inertia_mean - params.inertia_observed)/params.inertia_uncertainty, 4)} times the uncertainty.")

print(f"\nMean density: {round(meanDensity_mean, 1)} kg/m^3")
print(f"Observed mean density: {params.meanDensity_observed} plus/minus {params.meanDensity_uncertainty} kg/m^3")
print(f"Mean density deviation from observed value: {round(abs(meanDensity_mean - params.meanDensity_observed), 1)} kg/m^3, {round(abs(meanDensity_mean - params.meanDensity_observed)/params.meanDensity_uncertainty, 3)} times the uncertainty.")

print("\n--- CALCULATED VALUES ---")
print("Center pressure: ", p_mean[0]/1000000000, " GPa")
print("Gravitational acceleration at surface: ", g_mean[-1], " m/s^2")

print("\n--- INTERNAL COMPOSITION ---")
print("Core radius: ", core_boundary_mean/1000, " km")
print("Mantle thickness: ", (mantle_boundary_mean - core_boundary_mean)/1000, " km")
print("Crust thickness: ", (params.rtotal-mantle_boundary_mean)/1000, " km")

M_max, g_max, p_max, r_max, rho_max, T_max, core_boundary_max, mantle_boundary_max, inertia_max, simcount_max, meanDensity_max, core_mantle_boundary_temp_max, core_mantle_boundary_pressure_max, core_mantle_boundary_gravity_max, mantle_shell_boundary_temp_max, mantle_shell_boundary_pressure_max, mantle_shell_boundary_gravity_max = functions.iterate(M_max, g_max, p_max, r_max, rho_max, T_max)

# Print final results
print('\n---SIMULATION COMPLETE - MAX TEMP---')
print(f"Number of iterations: {simcount_max}")

print("\n--- COMPARISON TO OBSERVED VALUES ---")
print(f"Total mass: {M_max[-1]:.3e} kg")
print(f"Observed mass: {params.M_observed} plus/minus {params.M_uncertainty} kg")
print(f"Mass deviation from observed value: {abs(M_max[-1] - params.M_observed):.3e} kg, {round(abs(M_max[-1] - params.M_observed)/params.M_uncertainty, 3)} times the uncertainty.")

print(f"\nMoment of inertia factor: {round(inertia_max, 3)}")
print(f"Observed moment of inertia factor: {params.inertia_observed} plus/minus {params.inertia_uncertainty}")
print(f"Moment of inertia factor deviation from observed value: {round(abs(inertia_max - params.inertia_observed), 4)}, {round(abs(inertia_max - params.inertia_observed)/params.inertia_uncertainty, 4)} times the uncertainty.")

print(f"\nMean density: {round(meanDensity_max, 1)} kg/m^3")
print(f"Observed mean density: {params.meanDensity_observed} plus/minus {params.meanDensity_uncertainty} kg/m^3")
print(f"Mean density deviation from observed value: {round(abs(meanDensity_max - params.meanDensity_observed), 1)} kg/m^3, {round(abs(meanDensity_max - params.meanDensity_observed)/params.meanDensity_uncertainty, 3)} times the uncertainty.")

print("\n--- CALCULATED VALUES ---")
print("Center pressure: ", p_max[0]/1000000000, " GPa")
print("Gravitational acceleration at surface: ", g_max[-1], " m/s^2")

print("\n--- INTERNAL COMPOSITION ---")
print("Core radius: ", core_boundary_max/1000, " km")
print("Mantle thickness: ", (mantle_boundary_max - core_boundary_max)/1000, " km")
print("Crust thickness: ", (params.rtotal-mantle_boundary_max)/1000, " km")

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

