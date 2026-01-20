import random
import params
import model1
import statistics

n = 10
initial_coreBoundaries = []
initial_mantleBoundaries = []
final_coreBoundaries = []
final_mantleBoundaries = []

for i in range(0,n):
    print(f"Starting iteration {i} out of {n}")
    # TODO: make it so that the program can only chose values on an interval of delta_r
    core_boundary = random.uniform(550.0e3, 950.0e3)
    mantle_boundary = random.uniform(1300.0e3, 1500.0e3)
    initial_coreBoundaries.append(core_boundary)
    initial_mantleBoundaries.append(mantle_boundary)

    core_boundary, mantle_boundary = model1.Model1(core_boundary, mantle_boundary)
    final_coreBoundaries.append(core_boundary)
    final_mantleBoundaries.append(mantle_boundary)

print(f"Initial core boundaries: {initial_coreBoundaries}")
print(f"Final core boundaries: {final_coreBoundaries}")
print(f"Initial mantle boundaries: {initial_mantleBoundaries}")
print(f"Final mantle boundaries: {final_mantleBoundaries}")

print(f"\nStandard deviation of initial core boundaries: {statistics.stdev(initial_coreBoundaries)}")
print(f"Standard deviation of final core boundaries: {statistics.stdev(final_coreBoundaries)}")
print(f"Standard deviation of initial mantle boundaries: {statistics.stdev(initial_mantleBoundaries)}")
print(f"Standard deviation of final mantle boundaries: {statistics.stdev(final_mantleBoundaries)}")

