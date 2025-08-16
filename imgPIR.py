#  imgPIR.py

import serial,re,time
import pygame
import pygame.camera
from pygame.locals import *

def main(args):
    ser_r = serial.Serial('/dev/ttyACM0', 9600, timeout=0.050)
    r1 = re.compile(".*Motion detected!")
    #r2 = re.compile(".*cm")
    while True:
        read_serial = ser_r.readline()
        if (read_serial):
            read_serial = read_serial.decode("utf-8")
            #print(read_serial)
            i = r1.search(read_serial)
            if (i):
                print ("Taking pic")
                #capImg()
                pygame.init()
                pygame.camera.init()
                camlist = pygame.camera.list_cameras()
                print(camlist)
                if camlist:
                    cam = pygame.camera.Camera(camlist[0],(640,480))
                cam = pygame.camera.Camera("/dev/video0",(640,480))
                cam.start()
                time.sleep(3)
                image = cam.get_image()
                time.sleep(3)
                cam.stop()
                #time.sleep(3)
                pygame.image.save(image, "image.jpeg")
                time.sleep(5) # Sleep for 5 seconds
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
