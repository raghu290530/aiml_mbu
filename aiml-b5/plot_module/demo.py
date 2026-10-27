#  pip install matplotlib
import matplotlib.pyplot as plt
import numpy as np

# x = np.array([0,3])
# y = np.array([0,3])

# x = np.array([-5,8])
# y = np.array([0,3])

x = np.array([0,3,5,9,10])
y = np.array([0,8,6,4,3])

plt.plot(x,y,'P-.g',ms=20,
         mec='r',mfc='y',lw=2)
plt.show()