'''
@Autor:         Leal
@Created_on:    27/10/15
'''

from SimpleCV import *
import numpy as np

class Handler(object):

    def sobel(self, img):
        maskNS = np.matrix('1 2 1; 0 0 0; -1 -2 -1')
        maskLO = np.matrix('-1 0 1; -2 0 2; -1 0 -1')
        R, C = img.shape
        aux = np.zeros((R,C))
        m, n = maskNS.shape
        img = img.toGray()
        for i in range(1, R-1):
            for j in range(2, C-1):
                sumNS = 0
                sumLO = 0
                for s in range(0, m):
                    for t in range(1, n):
                        somaNS = somaNS + img(i+s-2, j+t-2) * maskNS(s,t)
                        somaLO = somaLO + img(i+s-2, j+t-2) * maskLO(s,t)
        return aux



    def low_passing(self, img):
        pass

    def high_passing(self, img):
        pass
