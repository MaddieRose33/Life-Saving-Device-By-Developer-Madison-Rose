#!/usr/bin/python

#
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


try: #if it runs a specific tkinter on the wrong version there will be an error so this prevents that (it still might occur later on)
    from tkinter import * #Python 3 is running
except:
    from Tkinter import * #Python2 is running
import os

from TextMessage import *

#user = os.environ.get("USERNAME") #Get the windows login name.

def getNumber():
    if E1.get().isdigit(): #Make sure input is a number then do the following indented code.
        try: #Try to make the directory/folder (This is in a try/except because if you already entered in a phone number and clicked submmit then wanted to
            os.makedirs("/home/pi/Desktop/PhoneNumber/") # switch it to a new phone number it gave an error. Now you can change it.
            pass
        except FileExistsError: #as stated above if you get an error and come to this code that means there is already a directory/phonenumber so replace the old with the new
            print("Replacing old phone number with new: " + E1.get())
        
        #The phone number is a digit
        #so store the phone number and tell the user
            
        #v storing the digit checked phone number v
        os.chdir("/home/pi/Desktop/PhoneNumber/")
        
        f = open("PhoneNumber.txt", "w+")
        
        f.write("+" + E1.get())
        f.close()
        #^ storing the digit checked phone number ^
        
        #v Notify the user that the phone number has been stored v
        print("Phone Number set to: " + E1.get())
        label3 = Label(root, text="Number now set to:" + E1.get()) #Local variable this cannot be accessed globally
        label3.pack()
        label4 = Label(root, text="A text message will be sent to your phone shortly to ensure that this is working.")
        label4.pack()
        
        Text("Test text message.")
        
        time.sleep(10)
        #^ Notify the user that the phone number has been stored ^
        
        # Reboot computer so that it will run line saying that it exists and start checking weight
        os.system("sudo reboot")
        
    else: #If it is a string then don't do anything but this code indented below.
        print(E1.get() + " is not a number. Please check your input.")
        label5 = Label(root, text=E1.get() + " is not a number. Please check your input.")
        label5.pack()
        
if not os.path.exists("/home/pi/Desktop/PhoneNumber/"): #If there is no phone number stored on the computer
    root = Tk() #Start setting up GUI
    root.title("Phone Number")
    label0 = Label(root, text="\n  Please enter a number for us to notify.  \n")
    label1 = Label(root, text="For Assistance Message: 18454670477")
    E1 = Entry(root, bd =5)
    
    label2 = Label(root, text="\n\nExample: 18452313212")
    submit = Button(root, text="Submit", command=getNumber) #When the user clicks submit button it will call the function getNumber and all of the code within that function.
    
    """v Packing GUI so it appears on screen v"""
    label0.pack()
    label1.pack()
    E1.pack()
    label2.pack()
    submit.pack(side=BOTTOM)
    root.mainloop()
    """^ Packing GUI so it appears on screen ^"""

if os.path.exists("/home/pi/Desktop/PhoneNumber/"): # There is a phone number stored.
    from Weight import *
    Weight()
    

"""
Code starts on line 31.
1. If the directory does not exist.
    Set up GUI
    onclick submit call function getNumber
    
    1.2. Clicked submit
        Go to line 11 for function getNumber
        If the input is a number
            try to make the directory
            except (if you get an error that means the directory/phone is already there (meaning you just put a number then wanted to switch it)) so replace the old number with the new one.
            go to the directory
            write in the phone number
            tell the user you changed the phone number
            close file
            
            reboot and go to 2.
            
        else: (the input they gave is not a number)
            tell them it's not a number and don't make the directory.
            
2. If the directory does exist
    call weight
    if there is weight
        call temp
        if temp is bad
            text then sleep then reboot just to wait a bit longer and because hey everyone needs a reboot every now and then right right guys??
"""
