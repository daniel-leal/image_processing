'''
@Autor:         Leal
@Created_on:    27/10/15
'''

from SimpleCV import *
from handler import *


if __name__ == '__main__':

    # init camera
    cam = Camera(prop_set={"width":600,"height":400})

    # init display
    disp = Display()

    # Show image while user didn't click
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

    # Instantiate handler object
    hnd = Handler()

    # Show and Save Image Histogram
    hnd.save_histogram(selfie)

    # Sobel Filter
    hnd.sobel('selfie.png')
