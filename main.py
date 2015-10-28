'''
@Autor:         Leal
@Created_on:    27/10/15
'''

from SimpleCV import *
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

    # create handler object
    filter_hnd = hnd.Handler()

    # Apply Filters
    lpf = filter_hnd.low_passing(selfie)
    #lpf.save('low_passing_selfie.png')

    hpf = filter_hnd.low_passing(selfie)
    #hpf.save('high_passing_selfie.png')

    sobel = filter_hnd.low_passing(selfie)
    #sobel.save('sobel_selfie.png')
