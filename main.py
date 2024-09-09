import cv2
import mediapipe as mp
import pyautogui
cap=cv2.VideoCapture(0)
hand_detector=mp.solutions.hands.Hands()
drawing_utils=mp.solutions.drawing_utils
screen_width, screen_height=pyautogui.size()

index_y=0 #given this to let the click funstion calculate the differnece between index and thumb
while True:
    _,frame=cap.read()
    frame=cv2.flip(frame,1)
    frame_height, frame_width, _=frame.shape
    rgb_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    output=hand_detector.process(rgb_frame)
    hands=output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame,hand)
            landmarks=hand.landmark
            for id, landmark in enumerate(landmarks):
                x=int(landmark.x*frame_width)    #roundig off for better understanding
                y=int(landmark.y*frame_height)
                # print(x,y)
                if id==8:#index finger tip 
                    cv2.circle(img=frame,center=(x,y),radius=20, color=(0,255,255))  #yellow color
                    index_x=screen_width/frame_width * x   #converting the coords to actual screen pixels
                    index_y=screen_height/frame_height * y  
                    pyautogui.moveTo(index_x,index_y)   #moves the cursor to the position of index finger tip
                if id==4:#thumb tip 
                    cv2.circle(img=frame,center=(x,y),radius=10, color=(0,0,255))   #blue color
                    thumb_x=screen_width/frame_width * x   #converting the coords to actual screen pixels
                    thumb_y=screen_height/frame_height * y  
                    # print(abs(index_y-thumb_y))
                    if abs(index_y-thumb_y)<20:
                        print('left click')
                        pyautogui.leftClick()
                        pyautogui.sleep(1)
                if id==12:#mid finger tip
                    cv2.circle(img=frame,center=(x,y),radius=10, color=(0,255,0))  #green color
                    mid_x=screen_width/frame_width * x   #converting the coords to actual screen pixels
                    mid_y=screen_height/frame_height * y  
                    # print(abs(mid_y-thumb_y))
                    if abs(mid_y-thumb_y)<20:
                        print('right click')
                        pyautogui.rightClick()
                        pyautogui.sleep(1)
                if id==20:#landmark 20 on pinkey finger
                    cv2.circle(img=frame,center=(x,y),radius=10, color=(0,255,0))  #green color
                    pinkey_x=screen_width/frame_width * x   #converting the coords to actual screen pixels
                    pinkey_y=screen_height/frame_height * y  
                    print(abs(pinkey_y-thumb_y))
                    if abs(pinkey_y-thumb_y)<20:
                        print('scroll up')
                        pyautogui.scroll(500)
                        pyautogui.sleep(1)
                if id==16:#landmark 16 on ring finger
                    cv2.circle(img=frame,center=(x,y),radius=10, color=(0,255,0))  
                    ring_x=screen_width/frame_width * x   #converting the coords to actual screen pixels
                    ring_y=screen_height/frame_height * y  
                    # print(abs(ring_y-thumb_y))
                    if abs(ring_y-thumb_y)<20:
                        print('scroll down')
                        pyautogui.scroll(-500)
                        pyautogui.sleep(1)
    # print(hands)
    cv2.imshow("MyVid",frame)
    cv2.waitKey(1)