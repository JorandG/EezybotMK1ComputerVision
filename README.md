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
