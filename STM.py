import numpy as np
from pylab import imshow,show

data = np.loadtxt('stm.txt', float)
imshow (data, origin="lower")
show() 