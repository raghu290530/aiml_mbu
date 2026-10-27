# pip install matplotlib
import matplotlib.pyplot as plt
import numpy as np

# x = np.array([0,5])
# y = np.array([0,5])

# x = np.array([6,15])
# y = np.array([0,-5])

x = np.array([0,2,6,5,7])
y = np.array([2,5,4,3,3])
plt.plot(x,y,'P-.m',
         ms=20,mec = 'y',
         mfc='b',linewidth=5)
plt.show()

y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])

plt.plot(y1,color='r')
plt.plot(y2,'o:b')

plt.show()