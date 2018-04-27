import os
import glob
import time

from TextMessage import *

#8-3-2017 Developer Madison
#THE DIRECTORY THIS IS IN IS /home/pi/temperature_sensor/


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

# Working temperature

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
 
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'
 
def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines
 
def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0

	# Make readable
        print_temp_f = str(temp_f).split(".")
        print_temp_f = print_temp_f[0]
        print_temp_f = str(print_temp_f).replace("'", "", 2)
        
	# Note additional sensor may remote start car and turn on climate control
        if temp_f >= 82:
            print("2 : Warning the temperature is getting hot! " + str(print_temp_f) + " F - Unsafe level!")
            Text("Warning the temperature is getting hot! " + str(print_temp_f) + " F - Unsafe level!")
        elif temp_f < 55:
            print("2 : Warning temperature is getting dangerously cold!" + str(print_temp_f) + " F - Unsafe level!")
            Text("Warning temperature is getting dangerously cold!" + str(print_temp_f) + " F - Unsafe level!")
            
        return temp_c, print_temp_f
	

#print(read_temp())
#time.sleep(1)
