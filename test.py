import numpy as np
import propagate

a = np.arange(0, 6+2, 2)
print(a)
b = np.ones(len(a))
for i in np.flip(range(1, len(a))):
    a[i-1] = a[i]+b[i-1]
    print(i)
print(a)