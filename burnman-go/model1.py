import numpy as np
import matplotlib.pyplot as plt
import functions
import params
import random

# Setting up arrays
M, g, p, r, rho = functions.create_arrays(params.rtotal)

# Setting the initial core and mantle boundaries. Can be changed by editing params.py
core_boundary = params.core_boundary
mantle_boundary = params.mantle_boundary

# Setting up a counter and a moment of inertia variable for the purpose of iterating over different core and mantle boundaries
simcount = 0
inertia = 0.0
meanDensity = 0

# Set initial mantle, core, and crust (ocean) densities
for i in range(len(r)):
        if r[i] <= core_boundary:
            rho[i] = params.density_core_Fe
        elif core_boundary < r[i] and r[i] <= mantle_boundary:
            rho[i] = params.density_mantle
        else:
            rho[i] = params.density_shell

# Start iteration
while abs(inertia - params.inertia_observed) > params.inertia_uncertainty or abs(M[-1] - params.M_observed) > params.M_uncertainty or abs(meanDensity - params.meanDensity_observed) > params.meanDensity_uncertainty: # continue iterating as long as moment of inertia or total mass deviate by more than 1% from observations
    simcount += 1
    print("Starting simulation ", simcount)

    # Integrating
    for i in range(0, len(r)-1):
        M[i+1] = functions.Mass(M[i], r[i+1], rho[i+1])

    for i in range(len(r)):
        g[i] = functions.Gravity(params.G, M[i], r[i])

    for i in np.flip(range(1, len(r))):
        p[i-1] = functions.Pressure(p[i], rho[i], g[i])
    
    #print('Residual moment of inertia: ', abs((inertia-params.inertia_observed)/params.inertia_observed*100), ' percent')
    #print('Residual mass: ', abs((M[-1]-params.M_observed)/params.M_observed*100), ' percent')

    # Adjust boundaries based on the difference between the observed and calculated mass and moment of inertia.
    # Increase the core size if the mass is too small, decrease the core size if the mass is too large.
    # Increase the mantle thickness if the moment of inertia is too small, decrease the mantle thickness if the moment of inertia is too large.
    if M[-1] > params.M_observed:
        factor = random.uniform(0.7, 1.3)*abs((M[-1] - params.M_observed)/params.M_uncertainty)
        dice = random.random()
        if dice > 0.5:
            core_boundary -= factor*params.delta_r
            if core_boundary <= 0:
                core_boundary = params.delta_r
        else:
            mantle_boundary -= factor*params.delta_r
            if mantle_boundary < core_boundary:
                mantle_boundary = core_boundary + params.delta_r
    elif M[-1] < params.M_observed:
        factor = random.uniform(0.7, 1.3)*abs((M[-1] - params.M_observed)/params.M_uncertainty)
        dice = random.random()
        if dice > 0.5:
            core_boundary += factor*params.delta_r
            if core_boundary > mantle_boundary:
                core_boundary = mantle_boundary - params.delta_r
        else:
            mantle_boundary += factor*params.delta_r
            if mantle_boundary >= params.rtotal:
                mantle_boundary = params.rtotal - params.delta_r
    
    # Calculate moment of inertia and compare to observations
    inertia = functions.inertia(r, rho, params.delta_r, M)
    
    if inertia > params.inertia_observed:
        factor = random.uniform(0.7, 1.3)*abs((inertia - params.inertia_observed)/params.inertia_uncertainty)
        dice = random.random()
        if dice > 0.5:
            mantle_boundary -= factor*params.delta_r
            if mantle_boundary < core_boundary:
                mantle_boundary = core_boundary + params.delta_r
        else:
            core_boundary -= factor*params.delta_r
            if core_boundary <= 0:
                core_boundary = params.delta_r
    elif inertia < params.inertia_observed:
        factor = random.uniform(0.7, 1.3)*abs((inertia - params.inertia_observed)/params.inertia_uncertainty)
        dice = random.random()
        if dice > 0.5:
            mantle_boundary += factor*params.delta_r
            if mantle_boundary >= params.rtotal:
                mantle_boundary = params.rtotal - params.delta_r
        else:
            core_boundary += factor*params.delta_r
            if core_boundary > mantle_boundary:
                core_boundary = mantle_boundary - params.delta_r
    
    # Recalculate density
    for i in range(len(r)):
        if r[i] <= core_boundary:
            rho[i] = params.density_core_Fe
        elif core_boundary < r[i] and r[i] <= mantle_boundary:
            rho[i] = params.density_mantle
        else:
            rho[i] = params.density_shell
    coreVolume = functions.sphereVolume(core_boundary)
    mantleVolume = functions.sphereShellVolume(core_boundary, mantle_boundary)
    shellVolume = functions.sphereShellVolume(mantle_boundary, params.rtotal)
    totalVolume = functions.sphereVolume(params.rtotal)

    meanDensity = (coreVolume*params.density_core_Fe + mantleVolume*params.density_mantle + shellVolume*params.density_shell)/totalVolume
    
    if meanDensity > params.meanDensity_observed:
        factor = random.uniform(0.7, 1.3)*abs((meanDensity - params.meanDensity_observed)/params.meanDensity_uncertainty)
        dice = random.random()
        if dice > 0.5:
            core_boundary -= factor*params.delta_r
            if core_boundary <= 0:
                core_boundary = params.delta_r
        else:
            mantle_boundary -= factor*params.delta_r
            if mantle_boundary < core_boundary:
                mantle_boundary = core_boundary + params.delta_r
    elif meanDensity < params.meanDensity_observed:
        factor = random.uniform(0.7, 1.3)*abs((meanDensity - params.meanDensity_observed)/params.meanDensity_uncertainty)
        dice = random.random()
        if dice > 0.5:
            core_boundary += factor*params.delta_r
            if core_boundary > mantle_boundary:
                core_boundary = mantle_boundary - params.delta_r
        else:
            mantle_boundary += factor*params.delta_r
            if mantle_boundary >= params.rtotal:
                mantle_boundary = params.rtotal - params.delta_r

# Plot pressure, mass, density, and gravity as a function of radius.   
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

# Print final results
print('\n------ SIMULATION COMPLETE ------')
print("Number of iterations: ", simcount)

print("\n--- COMPARISON TO OBSERVED VALUES ---")
print("Total mass: ", f"{M[-1]:.3e} kg")
print("Observed mass: ", params.M_observed, " plus/minus 1.5*10^20 kg")
print(f"Mass deviation from observed value: {abs(M[-1] - params.M_observed):.3e} kg, {round(abs(M[-1] - params.M_observed)/params.M_uncertainty, 3)} times the uncertainty.")

print("\nMoment of inertia factor: ", round(inertia, 3))
print("Observed moment of inertia factor: ", params.inertia_observed, " plus/minus 0.005")
print(f"Moment of inertia factor deviation from observed value: {round(abs(inertia - params.inertia_observed), 4)}, {round(abs(inertia - params.inertia_observed)/params.inertia_uncertainty, 4)} times the uncertainty.")

print("\nMean density: ", round(meanDensity, 1), " kg/m^3")
print("Observed mean density: ", params.meanDensity_observed, " plus/minus 1.7 kg/m^3")
print(f"Mean density deviation from observed value: {round(abs(meanDensity - params.meanDensity_observed), 1)} kg/m^3, {round(abs(meanDensity - params.meanDensity_observed)/params.meanDensity_uncertainty, 3)} times the uncertainty.")

print("\n--- CALCULATED VALUES ---")
print("Center pressure: ", p[0]/1000000000, " GPa")
print("Gravitational acceleration at surface: ", g[-1], " m/s^2")

print("\n--- INTERNAL COMPOSITION ---")
print("Core radius: ", core_boundary/1000, " km")
print("Mantle thickness: ", (mantle_boundary - core_boundary)/1000, " km")
print("Crust thickness: ", (params.rtotal-mantle_boundary)/1000, " km")

#for i in range(len(r)):
#    if r[i] <= core_boundary and r[i+1] > core_boundary: 
#        print("Gravitational acceleration at core-mantle boundary: ", g[i], " m/s^2")
#    elif r[i] <= mantle_boundary and r[i+1] > mantle_boundary:
#        print("Gravitational acceleration at mantle-shell boundary: ", g[i], " m/s^2")

# More final results




