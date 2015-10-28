'''
@Autor:         Leal
@Created_on:    27/10/15
'''

from SimpleCV import *
from pylab import *
import handler as hnd

if __name__ == '__main__':

    # init camera
    cam = Camera(prop_set={"width":600,"height":400})

    # init display
    disp = Display()

    # Show imagem while user didn't click
    while disp.isNotDone():
            # get webcam image
            img = cam.getImage()
            # save image and close when left click
            if disp.mouseLeft:
                    img.save('selfie.png')
                    break
            img.save(disp)


    # Load Image
    selfie = Image('selfie.png')

    # Show and Save Image Histogram
    gray = selfie.toGray()
    hist = gray.histogram(255)
    plot(hist)
    savefig('hist.png')

    # instantiate handler object
    filter_hnd = hnd.Handler()
