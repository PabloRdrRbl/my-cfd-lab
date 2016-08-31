import numpy as np
import matplotlib.pyplot as plt


# Grid parameters

N = 20  # Number of intervals
Nt = 360  # Number of time steps
dy = 1 / (N)  # Non-dimensional problem

u = np.zeros(N + 1)
y = np.linspace(0, 1, N + 1)

# Flow parameters

Re = 5000
sigma = 0.5
dt = sigma * dy**2 * Re


# Initial conditions

# This will be used as boundary condittion too. Same
# Applies to the no slip condition explicitly asumed
# using np.zeros()
u[-1] = 1  # Non-dimensional problem

# Plotting

#plt.figure()

# Time marching solution

for t in range(Nt):

    u[1: -1] = u[1: -1] + (dt / dy**2 / Re) * (u[2:] - 2 * u[1: -1] + u[:-2])

print(u)

np.savetxt('explicit%d.out' % (Nt), u, delimiter=',')
