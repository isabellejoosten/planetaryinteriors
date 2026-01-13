import numpy as np
import matplotlib.pyplot as plt
import functions
import params
import statistics
import pandas as pd
import seaborn as sb

# Setting up arrays
results = []

# Setting the core and mantle boundaries.
layerBoundaries = functions.create_layerheights()
M, g, p, r, rho = functions.create_arrays()

simcount = 0

coreRadii = np.arange(0, params.rtotal + params.delta_r, params.delta_r)
mantleRadii = np.arange(0, params.rtotal + params.delta_r, params.delta_r)

# Start iteration
dataframes = []
for coreRadius in layerBoundaries[1:]:
    for iteration in coreRadius[1:]:
        simcount += 1
        #print("Starting simulation ", simcount)
        if iteration[0] > iteration[1]:
            results = pd.DataFrame({'MOI':np.nan, 'coreBound':iteration[0], 'mantleBound':iteration[1], 'massDeviation':np.nan, 'MOIdeviation':np.nan}, index=[simcount])
        else:
            # Set mantle, core, and crust (ocean) densities
            rho = functions.set_density(rho, r, iteration[0], iteration[1])
            results = functions.iterate(M, g, p, r, rho, iteration[0], iteration[1], simcount)
        dataframes.append(results)

data = pd.concat(dataframes)
print(data['massDeviation'].std())



'''
cores = []
maxmantle = []
for i in range(len(listOfDicts)):
    cores.append(listOfDicts[i]['coreBound'])
    maxmantle.append(params.rtotal - listOfDicts[i]['coreBound'])
'''

'''
fig, ax = plt.subplots()
ax.fill_between(cores, cores, color='black')
im = ax.imshow(results_all, origin='lower', extent=[0, layerBoundaries[-1][-1][0], 0, layerBoundaries[-1][-1][1]], interpolation='bilinear')

# Show all ticks and label them with the respective list entries
startx, stopx = ax.get_xlim()
starty, stopy = ax.get_ylim()
ax.set_xticks(np.arange(startx, stopx, 200000))
ax.set_yticks(np.arange(starty, stopy, 200000))
ax.set_xlabel('Core radius')
ax.set_ylabel('Mantle outer radius')

cbar = ax.figure.colorbar(im, ax=ax)
cbar.ax.set_ylabel('Deviation', rotation=-90, va="bottom")

# Loop over data dimensions and create text annotations.
#for i in range(len(coreRadii)):
#    for j in range(len(mantleRadii)):
#        text = ax.text(j, i, results_all[i, j],
#                       ha="center", va="center", color="w")

ax.set_title("Mass and MOI deviation as a function of core radius and mantle outer radius")
#fig.tight_layout()
plt.show()
'''

