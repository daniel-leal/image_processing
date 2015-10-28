'''
@Autor:         Leal
@Created_on:    27/10/15
'''

from SimpleCV import *
from pylab import *
import scipy
from scipy import ndimage

class Handler():

    def save_histogram(self, img):
        gray = img.toGray()
        hist = gray.histogram(255)
        plot(hist)
        savefig('hist.png')

    def sobel(self, img):
        fig = scipy.misc.imread(img).astype('int32')
        dx = ndimage.sobel(fig, 0) # horizontal derivative
        dy = ndimage.sobel(fig, 1) # vertical derivative
        mag = np.hypot(dx, dy) # magnitude
        mag *= 255.0 / np.max(mag) # normalize
        scipy.misc.imsave('sobel.png', mag)
