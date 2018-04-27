# Life-Saving-Device
Open Source Code: Life saving device for infants and toddlers. Finally no more forgotten infants or toddlers in hot cars

Developed by: Madison Rose Lucey
Website for project: https://www.change.org/p/tom-marino-petition-to-prevent-infant-toddler-car-heatstroke-in-the-usa-more-than-36-kids-die-in-hot-cars-every-year-and-there-is-a-solution

Additional features that can work concurrently are 
#1 video live stream from passenger dash-cam of the toddler who may possibly be possibly facing a hyperthermia situation to parents phone. 
#2 One of the many available smartphone app's such as Linkr Mobile from Omega would enable a parent/caregiver to then in response remotely lock or unlock vehicle doors for rescue personnel and even remote start the vehicle from any location thus enabling AC/ Climate Control to maintain vehicle at an appropriate temperature 
#3 The app additionally provides GPS location that could be forwarded to emergency personnel.


Overview on how the code works: 
The code starts with Entry.py which will prompt the care-giver via GUI to enter their own phone number. The Raspberry PI then restarts.

Weight.py will wait till the seat is occupied then when it is move to tempsensor.py
tempsensor.py will check if the temp is above the pre-set temperature. If so send out alert notification to the caregivers phone number.

Wait a minute or two then check again.


Other files such as the ones listed below are demonstration files used for development mode, not required in the final product
cpu.py is a demonstration on how the raspberry pi may check it's own temperature.
Del.py Used by a developer to remove the current phone number. Must be run in sudo mode through terminal