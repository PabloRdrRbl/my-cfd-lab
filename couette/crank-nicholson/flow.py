import numpy as np
import matplotlib.pyplot as plt

import thomas


# Grid parameters

N = 20 # Number of intervals
Nt = 360 # Number of time steps
dy = 1 / (N)  # Non-dimensional problem

u = np.zeros(N + 1)
y = np.linspace(0, 1, N + 1)

# Flow parameters

E = 1
Re = 5000
dt = E * Re * dy**2

A = - E / 2
B = 1 + E

K = np.empty(N - 1)

# Initial conditions

# This will be used as boundary condittion too. Same
# Applies to the no slip condition explicitly asumed
# using np.zeros()
u[-1] = 1  # Non-dimensional problem

# Plotting

#plt.figure()

# Coefficient matriz

# Actually what we have are three diagonals, and two of them
# are equal, so we have main diagonal and other one

# We do not use boundaries
d = np.ones(N - 1) * B
dd = np.ones(N - 1) * A

# Time marching solution

for t in range(Nt):
    # Actually we do not use the boundary points in the solution
    K = (1 - E) * u[1: -1] + 0.5 * E * (u[2:] + u[:-2])

    # K and b (from the linear system solution) are differen but we use
    # K to compute b. Now K will be b
    K[-1] = K[-1] - A * u[-1]

    u[1: -1] = thomas.tridiagonal(d.copy(), dd.copy(), dd.copy(), K.copy())

print(u)

np.savetxt('implicit%d.out' % (Nt), u, delimiter=',')
