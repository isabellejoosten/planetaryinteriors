import numpy as np
import matplotlib.pyplot as plt
import functions
import params

# Setting up arrays
results = []

# Setting the core and mantle boundaries.
core_boundaries, mantle_boundaries = functions.create_layerheights()
M, g, p, r, rho = functions.create_arrays()

simcount = 0

# Start iteration
#while abs((inertia-params.inertia_observed)/params.inertia_observed*100) > 1.0 or abs((M[-1]-params.M_observed)/params.M_observed*100) > 1.0: # continue iterating as long as moment of inertia or total mass deviate by more than 1% from observations
for core_boundary in core_boundaries:
    x_array = np.array()
    for mantle_boundary in mantle_boundaries:
        simcount += 1
        print("Starting simulation ", simcount)

        # Set mantle, core, and crust (ocean) densities
        rho = functions.set_density(rho, r, core_boundary, mantle_boundary)
        dict = functions.iterate(M, g, p, r, rho, core_boundary, mantle_boundary, simcount)
        results.append(dict)
        np.append(x_array, )

matching = []
for profile in results:
    if abs(profile['massDeviation']) < 0.1 and abs(profile['MOIdeviation']) < 0.1:
        matching.append(profile)



print(len(matching))
print(matching[0])

fig, ax = plt.subplots()
im = plt

ax.set_title("Mass deviation")
fig.tight_layout()
plt.show()