import mediapipe as mp
import cv2
import time

cap = cv2.VideoCapture(0)

mpHand = mp.solutions.hands
#static_image_mode ==> boolean , false => detect , true => track
#max_num_hands = (default)1
#min_detection_confidence , min_tracking_confidence ==> interval (0,50)  detection ve tracking arasındaki değer 
# %100 ==> tracking   %0 ==> detection
hands = mpHand.Hands(max_num_hands=4)

mpDraw = mp.solutions.drawing_utils
pTime = 0
cTime = 0
while True:
    success , img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    results = hands.process(imgRGB)
    print(results.multi_hand_landmarks)  
    
    if (results.multi_hand_landmarks):
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handLms , mpHand.HAND_CONNECTIONS)    
            for id,lm in enumerate(handLms.landmark):
                # print(id , lm)
                h, w ,c = img.shape
                
                cx ,cy = int(lm.x*w) , int(lm.y*h)
                
                #bilek
                if id == 8:
                    cv2.circle(img , (cx,cy) , 9 , (255,0,0) , cv2.FILLED )
                    
    #fps
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, "FPS" + str(int(fps)), (10,75) , cv2.FONT_HERSHEY_PLAIN , 3 , (255,0,0))                
    cv2.imshow("img", img)
    cv2.waitKey(1)
    
    


    