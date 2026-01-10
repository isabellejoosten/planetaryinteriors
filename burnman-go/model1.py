import numpy as np
import matplotlib.pyplot as plt
import functions
import params

# Setting up arrays
results = []

# Setting the core and mantle boundaries.
layerBoundaries = functions.create_layerheights()
M, g, p, r, rho = functions.create_arrays()

simcount = 0

coreRadii = np.arange(0, params.rtotal + params.delta_r, params.delta_r)
mantleRadii = np.arange(0, params.rtotal + params.delta_r, params.delta_r)

# Start iteration
#while abs((inertia-params.inertia_observed)/params.inertia_observed*100) > 1.0 or abs((M[-1]-params.M_observed)/params.M_observed*100) > 1.0: # continue iterating as long as moment of inertia or total mass deviate by more than 1% from observations
listOfDicts = []
results_all = np.empty((0, len(layerBoundaries[0])-1))
for coreRadius in layerBoundaries[1:]:
    results_sameCore = np.empty((0))
    for iteration in coreRadius[1:]:
        simcount += 1
        print("Starting simulation ", simcount)

        if iteration[0] < iteration[1] and iteration[0] + iteration[1] <= params.rtotal:
            # Set mantle, core, and crust (ocean) densities
            rho = functions.set_density(rho, r, iteration[0], iteration[1])
            results = functions.iterate(M, g, p, r, rho, iteration[0], iteration[1], simcount)
            listOfDicts.append(results)
            results_sameCore = np.concatenate((results_sameCore, np.array([abs(results['massDeviation']*results["MOIdeviation"])])))
        else:
            print("Invalid combination of radii skipped")
            results_sameCore = np.concatenate((results_sameCore, np.array([0.1])))
    results_all = np.concatenate((results_all, [results_sameCore]))
print(results_all)


fig, ax = plt.subplots()
im = ax.imshow(results_all)

# Show all ticks and label them with the respective list entries
#ax.set_xticks(range(0, len(coreRadii), 10*params.delta_r), labels=coreRadii,
#              rotation=45, ha="right", rotation_mode="anchor")
#ax.set_yticks(range(len(mantleRadii)), labels=mantleRadii)

cbar = ax.figure.colorbar(im, ax=ax)
cbar.ax.set_ylabel('Deviation', rotation=-90, va="bottom")

# Loop over data dimensions and create text annotations.
#for i in range(len(coreRadii)):
#    for j in range(len(mantleRadii)):
#        text = ax.text(j, i, results_all[i, j],
#                       ha="center", va="center", color="w")

ax.set_title("Mass and MOI deviation as a function of core radius and mantle outer radius")
fig.tight_layout()
plt.show()


