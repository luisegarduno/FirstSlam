#!/usr/bin/env python3
import time
import cv2

# Set Width & Height: 960x540
W = 1920//2
H = 1080//2

def process_frame(img):
    # Resize video
    img = cv2.resize(img, (W, H))
    cv2.imshow('image', img)

    print("Resolution: ", img.shape)

if __name__ == "__main__":
    # Load video
    cap = cv2.VideoCapture("./Videos/driving.mp4")

    while cap.isOpened():
        ret, frame = cap.read()
        if ret == True:
            process_frame(frame)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        else:
            break

