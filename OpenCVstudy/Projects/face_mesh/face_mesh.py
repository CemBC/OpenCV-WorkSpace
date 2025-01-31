import cv2
import time
import mediapipe as mp

cap = cv2.VideoCapture("video1.mp4")

mpFace = mp.solutions.face_mesh
faceMesh = mpFace.FaceMesh(max_num_faces= 1)
mpDraw = mp.solutions.drawing_utils
drawSpec = mpDraw.DrawingSpec(thickness= 1 , circle_radius= 1 )
pTime = 0
while True:
    success , img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    results = faceMesh.process(imgRGB)
    print(results.multi_face_landmarks)
    
    if results.multi_face_landmarks:
        for faceLms in results.multi_face_landmarks:
            mpDraw.draw_landmarks(img, faceLms , mpFace.FACEMESH_TESSELATION , drawSpec , drawSpec)
            #mpDraw.draw_landmarks(img, faceLms , mpFace.FACEMESH_CONTOURS , drawSpec )
            #mpDraw.draw_landmarks(img, faceLms , mpFace.FACEMESH_TESSELATION , drawSpec )
         
        for id , lm in enumerate(faceLms.landmark):
            h , w , _ = img.shape
            cx , cy = int(lm.x * w ) , int(lm.y * h)
            print([id , cx , cy])
    
    cTime = time.time()
    fps = 1 / (cTime-pTime)
    pTime = cTime
    cv2.putText(img, "FPS:" + str(int(fps)), (10,65), cv2.FONT_HERSHEY_PLAIN, 2, (255,0,0) , 3 )
    cv2.imshow("img", img)
    cv2.waitKey(10)