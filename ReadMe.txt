This project is for  educational purposes only.
It provides a glimpse of openCV and mediapipe

The project can do the following functionalities:
1. Take the cursor anywhere---Index Finger
2. Left click---thumb + index finger
3. Right click---thumb + middle finger
4. Scroll down---thumb + ring finger
5. Scroll up--- thumb + pinky finger


Following are the steps:
step 1:
check your cam, enable and check if you can see yourself using the above code of CV2

step 2:
now we need to make the CV sense our hand movement, this can be done using mediapipe, so import mediapipe, use its functions

step 3:
seperate fingers for the  gesture recognition. landmarks are given on the internet
give index finger a color landmar of index finger top=8

step 4:
importing pyautogui you need to fed the position of your index finger i.e. x,y to let the cursor move inside the frame only
to let the cursor move outside the frame you need to do the following, (len_screen/len_frame)*x and same for y
this is bcz we obviously have to control the cursor on the screen

step 5:
now add functionality to the  mouse movement according to the distance between the tips of thumb and fingers
as per you like

step 6: 
pip install pyinstaller
pyinstaller main.py


https://stackoverflow.com/questions/18713086/virtualenv-wont-activate-on-windows