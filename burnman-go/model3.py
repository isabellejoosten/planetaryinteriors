import numpy as np
import matplotlib.pyplot as plt
import burnman
from burnman import Mineral, PerplexMaterial, Composite, Layer, Planet
from burnman import minerals
import params
from model1 import g as model1_g
from model1 import r as model1_r
from model1 import rho as model1_rho
from model1 import p as model1_p
from model2 import g_mean as model2_g
from model2 import r_mean as model2_r
from model2 import rho_mean as model2_rho
from model2 import p_mean as model2_p
from model2 import T_mean as model2_T

from model2 import core_mantle_boundary_pressure_min 
from model2 import core_mantle_boundary_gravity_min, core_mantle_boundary_temp_min 
from model2 import mantle_shell_boundary_gravity_min, mantle_shell_boundary_pressure_min, mantle_shell_boundary_temp_min
from model2 import core_boundary_min, mantle_boundary_min

from model2 import core_mantle_boundary_pressure_mean, core_mantle_boundary_gravity_mean, core_mantle_boundary_temp_mean 
from model2 import mantle_shell_boundary_gravity_mean, mantle_shell_boundary_pressure_mean, mantle_shell_boundary_temp_mean
from model2 import core_boundary_mean, mantle_boundary_mean

from model2 import core_mantle_boundary_pressure_max, core_mantle_boundary_gravity_max, core_mantle_boundary_temp_max
from model2 import mantle_shell_boundary_pressure_max, mantle_shell_boundary_gravity_max, mantle_shell_boundary_temp_max
from model2 import core_boundary_max, mantle_boundary_max


#depths = np.linspace(2890e3, 670e3, 20)
core_material = minerals.SE_2015.bcc_iron()
mantle_material = minerals.SLB_2022.olivine(molar_fractions=(0.5, 0.5))
shell_material = minerals.HP_2011_ds62.h2oL()

europa_min_mass = 0
europa_mean_mass = 0
europa_max_mass = 0
europa_min_moi = 0
europa_mean_moi = 0
europa_max_moi = 0

cm_bound_min = params.core_boundary
ms_bound_min = params.mantle_boundary
while abs(europa_min_mass-params.M_observed)/params.M_observed*100 > 0.5:
    core_min = Layer(name='Core', radii=np.linspace(0, cm_bound_min))
    core_min.set_material(core_material)    
    core_min.set_temperature_mode(temperature_mode='user-defined',
                                  temperatures = np.linspace(params.core_temp_min, core_mantle_boundary_temp_min))
    core_min.set_pressure_mode(pressure_mode='self-consistent',
                               pressure_top=core_mantle_boundary_pressure_min,
                               gravity_bottom=0)
    core_min.make()

    mantle_min = Layer(name='Mantle', radii=np.linspace(cm_bound_min, ms_bound_min))
    mantle_min.set_material(mantle_material)
    mantle_min.set_temperature_mode(temperature_mode='user-defined',
                                  temperatures = np.linspace(core_mantle_boundary_temp_min, mantle_shell_boundary_temp_min))
    mantle_min.set_pressure_mode(pressure_mode='self-consistent',
                               pressure_top=mantle_shell_boundary_pressure_min,
                               gravity_bottom=core_mantle_boundary_gravity_min)
    mantle_min.make()

    shell_min = Layer(name='Shell', radii=np.linspace(ms_bound_min, params.rtotal))
    shell_min.set_material(shell_material)
    shell_min.set_temperature_mode(temperature_mode='user-defined',
                                  temperatures = np.linspace(mantle_shell_boundary_temp_min, params.surface_temp))
    shell_min.set_pressure_mode(pressure_mode='self-consistent',
                               pressure_top=0,
                               gravity_bottom=mantle_shell_boundary_gravity_min)
    shell_min.make()
    europa_min = Planet('Europa (minimum core temperature)', [core_min, mantle_min, shell_min], verbose=True)
    europa_min.make()

    if europa_min.mass > params.M_observed:
            cm_bound_min -= params.delta_r
    elif europa_min.mass < params.M_observed:
            cm_bound_min += params.delta_r
    if europa_min.moment_of_inertia_factor > params.inertia_observed:
            ms_bound_min -= params.delta_r
    elif europa_min.moment_of_inertia_factor < params.inertia_observed:
            ms_bound_min += params.delta_r






core_mean = Layer(name='Core', radii=np.linspace(0, core_boundary_mean))
core_mean.set_material(core_material)    
core_mean.set_temperature_mode(temperature_mode='user-defined',
                                  temperatures = np.linspace(params.core_temp_mean, core_mantle_boundary_temp_mean))
core_mean.set_pressure_mode(pressure_mode='self-consistent',
                               pressure_top=core_mantle_boundary_pressure_mean,
                               gravity_bottom=0)

core_max = Layer(name='Core', radii=np.linspace(0, core_boundary_max))
core_max.set_material(core_material)    
core_max.set_temperature_mode(temperature_mode='user-defined',
                                  temperatures = np.linspace(params.core_temp_max, core_mantle_boundary_temp_max))
core_max.set_pressure_mode(pressure_mode='self-consistent',
                               pressure_top=core_mantle_boundary_pressure_max,
                               gravity_bottom=0)

# The "make" method does the calculations to make the pressure and gravity self-consistent.
core_mean.make()
core_max.make()



mantle_mean = Layer(name='Mantle', radii=np.linspace(core_boundary_mean, mantle_boundary_mean))
mantle_mean.set_material(mantle_material)
mantle_mean.set_temperature_mode(temperature_mode='user-defined',
                                  temperatures = np.linspace(core_mantle_boundary_temp_mean, mantle_shell_boundary_temp_mean))
mantle_mean.set_pressure_mode(pressure_mode='self-consistent',
                               pressure_top=mantle_shell_boundary_pressure_mean,
                               gravity_bottom=core_mantle_boundary_gravity_mean)

mantle_max = Layer(name='Mantle', radii=np.linspace(core_boundary_max, mantle_boundary_max))
mantle_max.set_material(mantle_material)
mantle_max.set_temperature_mode(temperature_mode='user-defined',
                                  temperatures = np.linspace(core_mantle_boundary_temp_max, mantle_shell_boundary_temp_max))
mantle_max.set_pressure_mode(pressure_mode='self-consistent',
                               pressure_top=mantle_shell_boundary_pressure_max,
                               gravity_bottom=core_mantle_boundary_gravity_max)

mantle_mean.make()
mantle_max.make()


shell_mean = Layer(name='Shell', radii=np.linspace(mantle_boundary_mean, params.rtotal))
shell_mean.set_material(shell_material)
shell_mean.set_temperature_mode(temperature_mode='user-defined',
                                  temperatures = np.linspace(mantle_shell_boundary_temp_mean, params.surface_temp))
shell_mean.set_pressure_mode(pressure_mode='self-consistent',
                               pressure_top=0,
                               gravity_bottom=mantle_shell_boundary_gravity_mean)

shell_max = Layer(name='Shell', radii=np.linspace(mantle_boundary_max, params.rtotal))
shell_max.set_material(shell_material)
shell_max.set_temperature_mode(temperature_mode='user-defined',
                                  temperatures = np.linspace(mantle_shell_boundary_temp_max, params.surface_temp))
shell_max.set_pressure_mode(pressure_mode='self-consistent',
                               pressure_top=0,
                               gravity_bottom=mantle_shell_boundary_gravity_max)


shell_mean.make()
shell_max.make()

europa_mean = Planet('Europa (mean core temperature)', [core_mean, mantle_mean, shell_mean], verbose=True)
europa_max = Planet('Europa (maximum core temperature)', [core_max, mantle_max, shell_max], verbose=True)
europa_mean.make()
europa_max.make()

print("----- MINIMUM CORE TEMPERATURE: -----")
print("Europa's total mass: ", europa_min.mass, " [kg]")
print('Deviation from observed mass: ', abs(europa_min.mass-params.M_observed)/params.M_observed*100, "%")
print("Europa's moment of inertia factor: ", europa_min.moment_of_inertia_factor, " [-]")
print("Deviation from observed moment of inertia factor: ", abs(europa_min.moment_of_inertia_factor-params.inertia_observed)/params.inertia_observed*100, "%")

print("----- MEAN CORE TEMPERATURE: -----")
print("Europa's total mass: ", europa_mean.mass, " [kg]")
print('Deviation from observed mass: ', abs(europa_mean.mass-params.M_observed)/params.M_observed*100, "%")
print("Europa's moment of inertia factor: ", europa_mean.moment_of_inertia_factor, " [-]")
print("Deviation from observed moment of inertia factor: ", abs(europa_mean.moment_of_inertia_factor-params.inertia_observed)/params.inertia_observed*100, "%")

print("----- MAXIMUM CORE TEMPERATURE: -----")
print("Europa's total mass: ", europa_max.mass, " [kg]")
print('Deviation from observed mass: ', abs(europa_max.mass-params.M_observed)/params.M_observed*100, "%")
print("Europa's moment of inertia factor: ", europa_max.moment_of_inertia_factor, " [-]")
print("Deviation from observed moment of inertia factor: ", abs(europa_max.moment_of_inertia_factor-params.inertia_observed)/params.inertia_observed*100, "%")

fig = plt.figure(figsize=(8, 5))
ax = [fig.add_subplot(2, 2, i) for i in range(1, 5)]


bounds = np.array([[layer.radii[0]/1.e3, layer.radii[-1]/1.e3]
                   for layer in europa_mean.layers])
maxy = [10, 10, 2, 1500]
for bound in bounds:
    for i in range(4):
        ax[i].fill_betweenx([0., maxy[i]],
                            [bound[0], bound[0]],
                            [bound[1], bound[1]], alpha=0.2)


ax[0].plot(model1_r / 1.e3, model1_rho / 1.e3, linestyle='--', c='black', label='Model I')
ax[0].plot(model2_r / 1.e3, model2_rho / 1.e3, linestyle='-', c='red', label='Model II')
ax[0].plot(europa_mean.radii / 1.e3, europa_mean.density / 1.e3, label='Model III')
ax[0].set_ylabel('Density ($10^3$ kg/m$^3$)')
ax[0].legend()

# Make a subplot showing the calculated pressure profile
ax[1].plot(model1_r / 1.e3, model1_p / 1.e9, c='black', linestyle='--')
ax[1].plot(model2_r / 1.e3, model2_p / 1.e9, c='red', linestyle='-')
ax[1].plot(europa_mean.radii / 1.e3, europa_mean.pressure / 1.e9)
ax[1].set_ylabel('Pressure (GPa)')

# Make a subplot showing the calculated gravity profile
ax[2].plot(model1_r / 1.e3, model1_g, c='black', linestyle='--')
ax[2].plot(model2_r / 1.e3, model2_g, c='red', linestyle='-')
ax[2].plot(europa_mean.radii / 1.e3, europa_mean.gravity)
ax[2].set_ylabel('Gravity (m/s$^2)$')
ax[2].set_xlabel('Radius (km)')

# Make a subplot showing the calculated temperature profile
ax[3].plot(model2_r / 1.e3, model2_T, c='red', linestyle='-')
ax[3].plot(europa_mean.radii / 1.e3, europa_mean.temperature)
ax[3].set_ylabel('Temperature (K)')
ax[3].set_xlabel('Radius (km)')
ax[3].set_ylim(0.,)

# Finally, let's overlay some geotherms onto our model
# geotherm
#labels = ['Stacey (1977)',
#          'Brown and Shankland (1981)',
#          'Anderson (1982)',
#          'Alfe et al. (2007)',
#          'Anzellini et al. (2013)']

#short_labels = ['S1977',
#                'BS1981',
#                'A1982',
#                'A2007',
#                'A2013']

#ax[3].plot(planet_zog.radii / 1.e3,
#burnman.geotherm.stacey_continental(planet_zog.depth),
#linestyle='--', label=short_labels[0])
#mask = planet_zog.depth > 269999.
#ax[3].plot(planet_zog.radii[mask] / 1.e3,
#           burnman.geotherm.brown_shankland(planet_zog.depth[mask]),
#           linestyle='--', label=short_labels[1])
#ax[3].plot(planet_zog.radii / 1.e3,
#           burnman.geotherm.anderson(planet_zog.depth),
#           linestyle='--', label=short_labels[2])

#ax[3].scatter([planet_zog.layers[0].radii[-1] / 1.e3,
#               planet_zog.layers[1].radii[-1] / 1.e3],
#              [5400., 4000.],
#              linestyle='--', label=short_labels[3])

#mask = europa.pressure < 330.e9
#temperatures = Anz_interp(planet_zog.pressure[mask])
#ax[3].plot(planet_zog.radii[mask] / 1.e3, temperatures,
#           linestyle='--', label=short_labels[4])

#ax[3].legend()

for i in range(2):
    ax[i].set_xticklabels([])
for i in range(4):
    ax[i].set_xlim(0., max(europa_mean.radii) / 1.e3)
    ax[i].set_ylim(0., maxy[i])

fig.set_layout_engine('tight')
plt.show()