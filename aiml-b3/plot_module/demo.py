import matplotlib.pyplot as plt
import numpy as np
# x = np.array([0,3])
# y = np.array([0,3])

# x = np.array([-50,300])
# y = np.array([0,3])

x = np.array([1,2,6,3,5])
y = np.array([1,3,2,6,4])

plt.plot(x,y,'o-.y', ms=10,mec='r',mfc='b',color='g',linewidth='0.1')
plt.show()