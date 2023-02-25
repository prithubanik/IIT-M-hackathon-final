import cv2

cap = cv2.VideoCapture('FullSizerender.MOV')

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    ret, frame = cap.read()
    height, width, _ = frame.shape
    frame=cv2.resize(frame,(1200,700))
    roi = frame[0: 700,0: 1200]

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    dst = cv2.Canny(gray, 500, 100) # aplica o detector de bordas de Canny à imagem src


    # Display the resulting frame
    cv2.imshow('frame',dst)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()