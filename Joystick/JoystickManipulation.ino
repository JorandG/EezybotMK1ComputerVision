// Include the Servo library 
#include <Servo.h>
#include <math.h>

#define L1 80 //lengths are in mm
#define L2 80
#define L3 61
#define PI 3.14159

// Create a servo object 
Servo Servo1; 
Servo Servo2;

double x;
double y; 

int potpinx = 0;  // analog pin used to connect the Joystick
int valx;    // variable to read the value from the analog pin
int potpiny = 1;  // analog pin used to connect the potentiometer
int valy;    // variable to read the value from the analog pin

// move gripper to x,y,z,gripangle
void movexy(double x1,double y1)
{
    //inverse kinematics for joint angles (RADIANS)
    double t2 = PI - acos((L1 * L1 + L2 * L2 - x1 * x1 - y1 * y1 ) / (2 * L1 * L2));
    double t1 = atan2(y1, x1) + atan2((L2*sin(t2)),(L1+(L2*cos(t2))));

    //convert to degrees
    double t1deg = t1 / PI * 180;
    double t2deg = t2 / PI * 180;

    //convert joint angles to servo command angles
    int h = (360 - (2*t2deg))/2;
    int b = 15;
    int t1servo = 180 - t1deg;
    int t2servo = t1deg + h - b;

    
    Servo1.write(t1servo);
    Servo2.write(t2servo);
    delay(200);  // change this to make the motions faster or slower 
}

void setup() { 
   // We need to attach the servo to the used pin number 
   Servo1.attach(6); 
   Servo2.attach(9);
   movexy(50,50);
   delay(2000); 
   movexy(100,50);
   delay(2000);
}
void loop(){ 
  valx = analogRead(potpinx);            // reads the value of the joystick (value between 0 and 1023)
  valx = map(valx, 50, 1023, 0, 250);     // scale it to use it with the servo (value between 0 and 180
  valy = analogRead(potpiny);            // reads the value of the potentiometer (value between 0 and 1023)
  valy = map(valy, 0, 1023, 0, 225);     // scale it to use it with the servo (value between 0 and 180))

  //print the coordinates returned by the equations, set by the potentiometer
  Serial.println(x = valx-50);
  Serial.println(y = valy);
  movexy(x,y);     
}
