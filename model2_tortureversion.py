import numpy as np
import matplotlib.pyplot as plt
import functions
import functions
import params

M, g, p, r, rho = functions.create_arrays()
T_min = functions.create_temp_array('min', r)
T_mean = functions.create_temp_array('mean', r)
T_max = functions.create_temp_array('max', r)

layersizes_array = np.arange(0, params.rtotal+params.delta_r, params.delta_r)

for core_boundary in layersizes_array:
    for mantle_boundary in layersizes_array:
        for ocean_boundary in layersizes_array:
            if core_boundary + mantle_boundary + ocean_boundary <= params.rtotal and core_boundary <= mantle_boundary and mantle_boundary <= ocean_boundary:
                functions.integrate(M, g, p, r, rho, T_mean, core_boundary, mantle_boundary, ocean_boundary)

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

