''' Demo code to control RGBLED, Button '''

#import library module 
from trekkoGPS import RGBLED, BUTTON
import time

rgbLed = RGBLED()
button1 = BUTTON(7)
button2 = BUTTON(15) 


def blinkRGB():
    #pixelon(arg1, arg2) arg1 = R, G, B color , arg2 = brightness value 0 - 1(Full)
    rgbLed.pixelon(color=(200, 200, 0), brightness=0.1)
    time.sleep(0.5)
    rgbLed.pixeloff()
    time.sleep(0.5)
    rgbLed.pixelon()  #default white color
    time.sleep(1)
    rgbLed.pixelon((120, 0, 120),0.5)
    time.sleep(0.5)

blinkRGB()

while 1:
    val1 = button1.read()
    val2 = button2.read()
    print("Bt1", val1)
    print("Bt2", val2)
    
    if val1 == 0:
        print("Button1 Pressed")
        rgbLed.pixelon(color=(200, 0, 0), brightness=0.3)
        
    if val2 == 1:
        print("Button2 Pressed")
        rgbLed.pixelon(color=(0, 200, 0), brightness=0.3)
        
    rgbLed.pixeloff()
    time.sleep(0.2)

