#!/usr/bin/env python3
import cv2
import numpy as np
from extractor import Extractor

# Set Width & Height: 960x540
W = 1920//2
H = 1080//2

fe = Extractor()

def process_frame(img):
    # Resize video
    img = cv2.resize(img, (W, H))

    # find the keypoints & compute the descriptors w/ ORB
    kps, des, matches = fe.extract(img)

    for p in kps:
        u,v = map(lambda x: int(round(x)), p.pt)
        cv2.circle(img, (u,v), color=(0,255,0), radius=3)

    # Show window
    cv2.imshow('TrySLAM', img)

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

