import numpy as np
import matplotlib.pyplot as plt
import functions
import functions
import params

results = []
core_boundaries, mantle_boundaries = functions.create_layerheights()
for core_boundary in core_boundaries:
    for mantle_boundary in mantle_boundaries:
        M, g, p, r, rho = functions.create_arrays(core_boundary, mantle_boundary)
        T = functions.create_temp_array('mean', r)
        dict = functions.iterate(M, g, p, r, rho, T, core_boundary, mantle_boundary)
        results.append(dict)

print(results)