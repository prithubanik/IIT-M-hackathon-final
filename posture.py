import cv2
import mediapipe as mp
import time


prev_frame_time = 0

new_frame_time = 0
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

pose = mp_pose.Pose(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5)

cap = cv2.VideoCapture(r"FullSizeRender.MOV")

while cap.isOpened():
    _, frame = cap.read()
    RGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    results = pose.process(RGB)
    print(results.pose_landmarks)


    mp_drawing.draw_landmarks(
    	frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
    gray = frame
 
    gray = cv2.resize(gray, (1280, 900))
 
    font = cv2.FONT_HERSHEY_SIMPLEX
    new_frame_time = time.time()

    fps = 1/(new_frame_time-prev_frame_time)
    prev_frame_time = new_frame_time
 
    fps = int(fps)
 

    fps = str(fps)
 
    
    cv2.putText(gray, fps, (7, 70), font, 3, (0, 255, 0), 3, cv2.LINE_AA)
 
    # displaying the frame with fps
    cv2.imshow('frame', gray)	
    if cv2.waitKey(1) == ord('q'):
    	
        cap.release()
        cv2.destroyAllWindows()