import cv2
import numpy as np

class Extractor(object):
    # detection
    def __init__(self):
        # Initiate ORB detector
        self.orb = cv2.ORB_create(100)
        self.bf = cv2.BFMatcher()
        self.last = None

    # extraction
    def extract(self, img):
        feats = cv2.goodFeaturesToTrack(np.mean(img, axis=2).astype(np.uint8), 3000, qualityLevel=0.01, minDistance=3)

        kps = [cv2.KeyPoint(x=f[0][0], y=f[0][1], size=20) for f in feats]
        kps, des = self.orb.compute(img, kps)

        # matching
        matches = None
        if self.last is not None:
            matches = self.bf.match(des, self.last['des'])
        self.last = {'kps': kps, 'des': des}

        return kps, des, matches
