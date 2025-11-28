import numpy as np
import matplotlib.pyplot as plt
import burnman
from burnman import Mineral, PerplexMaterial, Composite, Layer, Planet
from burnman import minerals
from model1 import g as model1_g
from model1 import r as model1_r
from model1 import rho as model1_rho
from model1 import p as model1_p
from model2 import g_mean as model2_g
from model2 import r_mean as model2_r
from model2 import rho_mean as model2_rho
from model2 import p_mean as model2_p
from model2 import T_mean as model2_T


#depths = np.linspace(2890e3, 670e3, 20)
core_material = minerals.SE_2015.bcc_iron()

core = Layer(name='Core', radii=np.linspace(0, 601e3))
core.set_material(core_material)    
core.set_temperature_mode(temperature_mode='adiabatic',
                                  temperature_top=932.)
core.set_pressure_mode(pressure_mode='self-consistent',
                               pressure_top=3.44e9,
                               gravity_bottom=0)

# The "make" method does the calculations to make the pressure and gravity self-consistent.
core.make()

mantle_material = minerals.SLB_2022.olivine(molar_fractions=(0.5, 0.5))

mantle = Layer(name='Mantle', radii=np.linspace(601e3, 1565e3-166e3))
mantle.set_material(mantle_material)
mantle.set_temperature_mode(temperature_mode='adiabatic',
                                  temperature_top=246.)
mantle.set_pressure_mode(pressure_mode='self-consistent',
                               pressure_top=0.36e9,
                               gravity_bottom=0.91)

mantle.make()

shell_material = minerals.HP_2011_ds62.h2oL()

shell = Layer(name='Shell', radii=np.linspace(1565e3-166e3, 1565e3))
shell.set_material(shell_material)
shell.set_temperature_mode(temperature_mode='adiabatic',
                                  temperature_top=104.)
shell.set_pressure_mode(pressure_mode='self-consistent',
                               pressure_top=0,
                               gravity_bottom=1.38)

shell.make()

europa = Planet('Europa', [core, mantle, shell], verbose=True)
europa.make()

print("Europa's total mass: ", europa.mass, " [kg]")
print("Europa's moment of inertia factor: ", europa.moment_of_inertia_factor, " [-]")


fig = plt.figure(figsize=(8, 5))
ax = [fig.add_subplot(2, 2, i) for i in range(1, 5)]


bounds = np.array([[layer.radii[0]/1.e3, layer.radii[-1]/1.e3]
                   for layer in europa.layers])
maxy = [10, 10, 2, 1000]
for bound in bounds:
    for i in range(4):
        ax[i].fill_betweenx([0., maxy[i]],
                            [bound[0], bound[0]],
                            [bound[1], bound[1]], alpha=0.2)


ax[0].plot(model1_r / 1.e3, model1_rho / 1.e3, linestyle='--', c='black', label='Model I')
ax[0].plot(model2_r / 1.e3, model2_rho / 1.e3, linestyle='-', c='red', label='Model II')
ax[0].plot(europa.radii / 1.e3, europa.density / 1.e3, label='Model III')
ax[0].set_ylabel('Density ($10^3$ kg/m$^3$)')
ax[0].legend()

# Make a subplot showing the calculated pressure profile
ax[1].plot(model1_r / 1.e3, model1_p / 1.e9, c='black', linestyle='--')
ax[1].plot(model2_r / 1.e3, model2_p / 1.e9, c='red', linestyle='-')
ax[1].plot(europa.radii / 1.e3, europa.pressure / 1.e9)
ax[1].set_ylabel('Pressure (GPa)')

# Make a subplot showing the calculated gravity profile
ax[2].plot(model1_r / 1.e3, model1_g, c='black', linestyle='--')
ax[2].plot(model2_r / 1.e3, model2_g, c='red', linestyle='-')
ax[2].plot(europa.radii / 1.e3, europa.gravity)
ax[2].set_ylabel('Gravity (m/s$^2)$')
ax[2].set_xlabel('Radius (km)')

# Make a subplot showing the calculated temperature profile
ax[3].plot(model2_r / 1.e3, model2_T, c='red', linestyle='-')
ax[3].plot(europa.radii / 1.e3, europa.temperature)
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
    ax[i].set_xlim(0., max(europa.radii) / 1.e3)
    ax[i].set_ylim(0., maxy[i])

fig.set_layout_engine('tight')
plt.show()