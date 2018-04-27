#Developer Madison
#8-2-2017


"""
   EMAIL ME FOR DETAILED DESCRIPTION OF HOW TO IMPLEMENT THE CODE WiTH TWILIO AND A MOBILE HOTSPOT
  MaddieRose1248@gmail.com

  This is free because it is important and needed.

  Last year in 2017 I developed a child car seat that can be used with the Raspberry PI 3 computer 
  that will detect if a child is left in a car so that no more children accidently get forgotten by caregivers in hot cars during the summer
  I wrote the code to work with my breadboard and a pressure and temperature sensor hooked up to my wireless device or any hotspot i.e phone 
  which can call pre-programmed numbers with a text message indicating that the child is in the car 
  and the temperature is rising or dropping to freezing. I plan to make a youtube video with more detailed description showing how this is 
  hooked up to a simple breadboard.
  I have been working on this for awhile but after seeing last week on the news that another child was left in a  
  hot car I decided to release it now. 
"""

# Working weight
from tempsensor import *

import RPi.GPIO as GPIO  
from time import sleep     # this lets us have a time delay (see line 15)

GPIO.setmode(GPIO.BCM)     # set up BCM GPIO numbering  
GPIO.setup(25, GPIO.IN)    # set GPIO25 as input (button)  
GPIO.setup(24, GPIO.OUT)   # set GPIO24 as an output (LED)

def Weight():  
    try:  
        while True:            # this will carry on until you hit CTRL+C  
            if GPIO.input(25): # if port 25 == 1  
                print("Port 25 is 1/HIGH/True - LED ON")
                GPIO.output(24, 1)         # set port/pin value to 1/HIGH/True
                
                print(read_temp())
                time.sleep(7)
                
            else:  
                print("Port 25 is 0/LOW/False - LED OFF")
                GPIO.output(24, 0)         # set port/pin value to 0/LOW/False  
            sleep(3)         # wait 0.1 seconds  
      
    finally:                   # this block will run no matter how the try block exits  
        GPIO.cleanup()         # clean up after yourself
        
        
        
        
        
        
        
         
        
