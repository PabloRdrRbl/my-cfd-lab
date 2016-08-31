import numpy as np
import matplotlib.pyplot as plt

i12 = np.genfromtxt('implicit12.out')
i60 = np.genfromtxt('implicit60.out')
i240 = np.genfromtxt('implicit240.out')
i360 = np.genfromtxt('implicit360.out')

e12 = np.genfromtxt('explicit12.out')
e60 = np.genfromtxt('explicit60.out')
e240 = np.genfromtxt('explicit240.out')
e360 = np.genfromtxt('explicit360.out')

plt.figure()

y = np.linspace(0, 1, 21)

plt.plot(i12, y, ls='--', marker='H', c='red', lw=2)
plt.plot(e12, y, ls='--', marker='H', c='blue', lw=2)

plt.plot(i60, y, ls='--', marker='o', c='red', lw=2)
plt.plot(e60, y, ls='--', marker='o', c='blue', lw=2)

plt.plot(i240, y, ls='--', marker='^', c='red', lw=2)
plt.plot(e240, y, ls='--', marker='^', c='blue', lw=2)

plt.plot(i360, y, ls='--', marker='D', c='red', lw=2)
plt.plot(e360, y, ls='--', marker='D', c='blue', lw=2)

plt.show()
