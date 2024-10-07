import cv2
import numpy as np
import datetime
import time
import Email as Mail
#import Shoter


body_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
upperbody_cascade = cv2.CascadeClassifier('haarcascade_upperbody.xml')
lowerbody_cascade = cv2.CascadeClassifier('haarcascade_lowerbody.xml')

def create_video():
    #cap = cv2.VideoCapture(0)

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

    print('Capturing...')
    start_time = time.time()
    while (int(time.time() - start_time) < 3):
        ret, frame = cap.read()

        frame = cv2.resize(frame, (640, 480))

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        body = body_cascade.detectMultiScale(gray, 1.3, 5)
        face = face_cascade.detectMultiScale(gray, 1.3, 5)
        upperbody = upperbody_cascade.detectMultiScale(gray, 1.3, 5)
        lowerbody = lowerbody_cascade.detectMultiScale(gray, 1.3, 5)

        for (x,y,w,h) in body:
            cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)
        for (x,y,w,h) in face:
            cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)
        for (x, y, w, h) in upperbody:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        for (x, y, w, h) in lowerbody:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        out.write(frame)
        cv2.imshow('frame', frame)

        frame = cv2.resize(frame, (160, 120))
        blur = cv2.medianBlur(frame, 3)
        fgmask = fgbg.apply(blur)

        cv2.waitKey(10)
    print('Video Captured!')
    #cap.release()
    cv2.destroyAllWindows()
    frame = np.zeros(frame.shape, np.uint8)
    return  fgmask


cap = cv2.VideoCapture(0)


kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
fgbg = cv2.createBackgroundSubtractorMOG2(history=50, varThreshold=50, detectShadows=False)

mailer = Mail.send_mail()
#shot = Shoter.make_shot()

while(1):

    ret, frame = cap.read()
    frame = np.zeros(frame.shape, np.uint8)
    ret, frame = cap.read()
    frame = cv2.resize(frame, (160, 120))

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.medianBlur(frame, 3)
    fgmask = fgbg.apply(blur)
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
    ret, thresh = cv2.threshold(fgmask, 150, 255, cv2.THRESH_BINARY)
    median = cv2.medianBlur(thresh, 3)

    rows = frame.shape[0]
    cols = frame.shape[1]

    num = 0
    for i in range (rows):
        for j in range (cols):
            if median[i][j] == 255:
                num = num + 1
                if num == 50:
                    print('Change Detected!')

                    fgmask = create_video()
                    print('Sending Email...')
                    #mailer.send()
                    print('Email Sent!')
                    break
            if num == 50:
                break

    print('End round!')
    cv2.imshow('frame', blur)
    cv2.imshow('bg', median)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


