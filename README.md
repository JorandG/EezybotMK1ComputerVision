# EezybotMK1ComputerVision

This project aims to use the open source robot manipulator EEZYbot MK1 of daGHIZmo with computer vision. A first part will be conducted in order to simply manipulate it with a joystick and then we will add the computer vision so that to end effector can follow an object. 

# Table of Contents

- [Introduction](#introduction)
- [Joystick Manipulation](#joystick-manipulation)
- [Computer Vision](#computer-vision)

# Introduction

The MK1 is a 3D printed robot manipulator that can be quite easily be assemble and cheaper so that why it was choosed for this project. It uses 4 SG90 servos and can be controlled from an arduino uno. The model and the assembly steps can be found here: 
[EEEZYbot MK1](http://www.eezyrobots.it/eba_mk1.html)

The robot arm has 4 DOF: waist/base, shoulder, elbow and gripper. In software, these are referred to as `base/BS`, `upDown/UD`, `frontBack/FB` and `gripper/GR` respectively.

![image](https://user-images.githubusercontent.com/91953623/136940677-a3ddd097-f937-48d2-92ac-823077375fb1.png)

# Joystick Manipulation

## Inverse Kinematic

The inverse kinematic allows to manipulate of robot for (x,y) coordinates. For a position you have to calculate the joints angles that your robot needs to have in order to reach that position, that what the equation of the inverse kinematic translates. For now the inverse kinematic used in the one describe here [Inverse Kinematic arduino](https://github.com/jamesthesken/eezy-control). You can find the inverse kinematic in the program Joystick.ino. 

## Installation

In order to manipulate the MK1 we used an arduino uno and a joystick as you can see on the following picture:

![MK1_Installation](https://user-images.githubusercontent.com/91953623/136943986-0263c297-68e9-40a3-beaf-8ac9bf2135f8.jpg)

The servos are plugged on the PWN pins 5, 6, 9. And the joystick is plugged on the A0 and A1. 

# Computer Vision

## Object Position

First of all we want to measure the position of an object on the table. For that task we are using OpenCV. 

You have to check the configuration, you should have the same versions as below or later.

```
$ pip list | grep -e opencv -e numpy
numpy                    1.17.5     
opencv-contrib-python    4.1.2.30   
opencv-python            4.1.2.30   

```
We start with the importations:

```
import cv2
import numpy as np
import cv2_imshow
```

We will print 4 aruco markers from 0 to 3 from the calibration: 

```
aruco = cv2.aruco
p_dict = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)
marker =  [0] * 4 #Initialisation
for i in range(len(marker)):
  marker[i] = aruco.drawMarker(p_dict, i, 75) # 75x75 px
  cv2.imwrite(f'marker{i}.png', marker[i])
```

The execution of this code should produce 4 file "marker0.png " to "marker3.png " that you will print and place in order to make a square of 15cm.
<img width="340" alt="aruco15" src="https://user-images.githubusercontent.com/91953623/136986057-0205ff8a-0c71-4b4f-8313-cd88a8b9d4f4.png">

We take a picture of your aruco markers and the object you want to localize, you rename it "inu.jpg":

This part of the program will transform you picture on a top view. 

```
aruco = cv2.aruco
p_dict = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)
img = cv2.imread('inu.jpg')
corners, ids, rejectedImgPoints = aruco.detectMarkers(img, p_dict) #détection

#Changer ici
corners2 = [np.empty((1,4,2))]*4
for i,c in zip(ids.ravel(), corners):
  corners2[i] = c.copy()
m[0] = corners2[0][0][2]
m[1] = corners2[1][0][3]
m[2] = corners2[2][0][0]
m[3] = corners2[3][0][1]

width, height = (500,500) #Taille de l'image après transformation
marker_coordinates = np.float32(m)
true_coordinates   = np.float32([[0,0],[width,0],[width,height],[0,height]])
trans_mat = cv2.getPerspectiveTransform(marker_coordinates,true_coordinates)
img_trans = cv2.warpPerspective(img,trans_mat,(width, height))
cv2_imshow(img_trans)
```

This is the result you should obtain: 
![result2](https://user-images.githubusercontent.com/91953623/136987572-ec906697-1689-4676-8aaf-16e789265b60.png)

Finally this part will give you th position of the object on the picture:



