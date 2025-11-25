import numpy as np
import matplotlib.pyplot as plt
import burnman
from burnman import Mineral, PerplexMaterial, Composite, Layer, Planet
from burnman import minerals


depths = np.linspace(2890e3, 670e3, 20)
rock = Composite([minerals.SLB_2011.mg_bridgmanite(),
                  minerals.SLB_2011.periclase()],
                 [0.8, 0.2])

lower_mantle = Layer(name='Lower Mantle', radii=6371.e3-depths)
lower_mantle.set_material(rock)
lower_mantle.set_temperature_mode(temperature_mode='adiabatic',
                                  temperature_top=1900.)
lower_mantle.set_pressure_mode(pressure_mode='self-consistent',
                               pressure_top=23.8e9,
                               gravity_bottom=10.7)

# The "make" method does the calculations to make the pressure and gravity self-consistent.
lower_mantle.make()

fig = plt.figure(figsize=(8, 8))
ax = [fig.add_subplot(2, 2, i) for i in range(1, 5)]
ax[0].plot(lower_mantle.pressure/1.e9, 6371.-lower_mantle.radii/1.e3)
ax[1].plot(lower_mantle.temperature, 6371.-lower_mantle.radii/1.e3)
ax[2].plot(lower_mantle.gravity, 6371.-lower_mantle.radii/1.e3)
ax[3].plot(lower_mantle.bullen, 6371.-lower_mantle.radii/1.e3)
for i in range(3):
    ax[i].set_ylim(6371.-lower_mantle.radii[0]/1.e3,
                   6371.-lower_mantle.radii[-1]/1.e3)
    ax[i].set_ylabel('Depth (km)')

ax[0].set_xlabel('Pressure (GPa)')
ax[1].set_xlabel('Temperature (K)')
ax[2].set_xlabel('Gravity (m/s$^2$)')
ax[3].set_xlabel('Bullen parameter')

fig.set_layout_engine('tight')