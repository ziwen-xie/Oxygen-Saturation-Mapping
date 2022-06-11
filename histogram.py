import numpy as np
import skimage.color
import skimage.io
import matplotlib.pyplot as plt

image = skimage.io.imread(fname = '/home/pi/SD/red.jpg',as_gray = True)

fig,ax = plt.subplots(2)
ax[0].imshow(image, cmap='gray')

histogram, bin_edges = np.histogram(image,bins = 256,range=(0,1))
ax[1].plot(bin_edges[0:-1],histogram)
plt.show()