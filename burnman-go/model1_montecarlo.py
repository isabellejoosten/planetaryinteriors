import random
import params
import model1
import statistics
import numpy as np
import time

start = time.time()
#import warnings
#warnings.filterwarnings("error")

all_initial_coreBoundaries = []
all_initial_mantleBoundaries = []
final_coreBoundaries = []
final_mantleBoundaries = []

n = 0
while n < 10:
    n += 1
    initial_coreBoundaries = np.arange(params.core_boundary - 5*params.delta_r, params.core_boundary + 6*params.delta_r, params.delta_r)
    initial_mantleBoundaries = np.arange(params.mantle_boundary - 5*params.delta_r, params.mantle_boundary + 6*params.delta_r, params.delta_r)
    i = 0

    #for i in range(0,n):
    for core in initial_coreBoundaries:
        for mantle in initial_mantleBoundaries:
            i += 1
            print(f"Starting simulation {i} out of {len(initial_coreBoundaries)*len(initial_mantleBoundaries)} on repeat {n} out of 10")
        # TODO: make it so that the program can only chose values on an interval of delta_r
            all_initial_coreBoundaries.append(core)
            all_initial_mantleBoundaries.append(mantle)

            core_boundary, mantle_boundary = model1.Model1(core, mantle)
            final_coreBoundaries.append(core_boundary)
            final_mantleBoundaries.append(mantle_boundary)


    #print(f"Initial core boundaries: {initial_coreBoundaries}")
    #print(f"Final core boundaries: {final_coreBoundaries}")
    #print(f"Initial mantle boundaries: {initial_mantleBoundaries}")
    #print(f"Final mantle boundaries: {final_mantleBoundaries}")

print("----- PROGRAM COMPLETED -----")
print(f"\nStandard deviation of initial core boundaries: {round(statistics.stdev(all_initial_coreBoundaries)/1000, 3)} km")
print(f"Standard deviation of final core boundaries: {round(statistics.stdev(final_coreBoundaries)/1000, 3)} km")
print(f"Mean of final core boundaries: {round(statistics.mean(final_coreBoundaries)/1000, 3)} km")
print(f"Median of final core boundaries: {round(statistics.median(final_coreBoundaries)/1000, 3)} km")
print(f"Minimum core boundary computed: {round(min(final_coreBoundaries)/1000, 3)}")
print(f"Maximum core boundary computed: {round(max(final_coreBoundaries)/1000, 3)}")

print(f"\nStandard deviation of initial mantle boundaries: {statistics.stdev(all_initial_mantleBoundaries)/1000} km")
print(f"Standard deviation of final mantle boundaries: {statistics.stdev(final_mantleBoundaries)/1000} km")
print(f"Mean of final mantle boundaries: {statistics.mean(final_mantleBoundaries)/1000} km")
print(f"Median of final mantle boundaries: {statistics.median(final_mantleBoundaries)/1000} km")
print(f"Minimum mantle boundary computed: {round(min(final_mantleBoundaries)/1000, 3)}")
print(f"Maximum mantle boundary computed: {round(max(final_mantleBoundaries)/1000, 3)}")

end = time.time()
print(f"Total time elapsed: {round((end - start)/60, 1)} minutes")

