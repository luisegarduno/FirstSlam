# TrySLAM

TrySLAM is a python program that applies SLAM (simultaneous localization and mapping) to a given video file.

## Prerequisites
* Have the following python3 modules installed: OpenCV & Numpy 

```bash
pip3 install opencv-python numpy
```

## Instructions
1. Edit [line 31](https://github.com/luisegarduno/TrySLAM/blob/38f5b280fc7a47d40d724c86ad024d772b94d382/slam.py#L31) of __slam.py__ with the location of the video you would like to use. By default, one has been supplied in the __Videos__ folder. 
2. Run program
```bash
./slam.py
```
3. Press 'q' at anytime to stop the program and close the video player. Otherwise the program will automatically stop once the video has played through once.
