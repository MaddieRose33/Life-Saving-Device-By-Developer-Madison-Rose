# Developer Madison Rose
# 4-26-2018

# vv IMPORTS vv
import os
from time import sleep
# ^^ IMPORTS ^^

"""
   EMAIL ME FOR DETAILED DESCRIPTION OF HOW TO IMPLEMENT THE CODE WITH TWILIO AND A MOBILE HOTSPOT
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


def Text(body):
    """ Send text message to care-givers phone. """

    # Try to import twilio if you can't then install it.
    from twilio.rest import Client

    # Navigate to phone number directory
    os.chdir("/home/pi/Desktop/PhoneNumber/")

    # put your own credentials here
    account_sid = "**************"
    auth_token = "*********************"
    client = Client(account_sid, auth_token)

    # Read care-giver phone number
    f = open("PhoneNumber.txt", "r+")
    PhoneNumber = f.read()

    # Send text message
    client.messages.create(
    to=PhoneNumber,
    from_="+***********",
    body = body)

    # Notify the user that the phone number has been stored and close file
    print("Phase 3 : Text Message Sent") 
    f.close()

    # Sleep then reboot
    sleep(60)
    os.system("sudo reboot")
