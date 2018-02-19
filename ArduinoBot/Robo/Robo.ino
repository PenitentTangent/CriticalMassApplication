//====== SERVO DEFINITIONS ==================

#include <Servo.h>

Servo servo;
int angle = 0;


//====== LIGHT SENSOR DEFINITIONS ===========

int colourPin = A0;

int touchPin = 8;


//====== MOTOR DEFINITIONS ==================
/*Define Motor Pins. R/L indicates left/right motor and F/R indicates whether
                  the robot moves forward or reverse when powered on pin.
  when looking at motor controller from top, leads away
  LF LR RF RR
*/
int LFSpeed = 0;
int LRSpeed = 0;
int RFSpeed = 0;
int RRSpeed = 0;
int minDist = 6;
int maxDist = 20;

#define motorLF 13
#define motorLR 12
#define motorRF 11
#define motorRR 10  //right side
#define motorFF 9
#define motorFR 8
// Drive Forward
void drive(int speed) {
  analogWrite(motorRF, 0);
  analogWrite(motorRR, 0);
  analogWrite(motorLF, 0);
  analogWrite(motorLR, 0);
  delay(10);

  LFSpeed = speed;
  RFSpeed = speed;
  analogWrite(motorRF, RFSpeed);
  analogWrite(motorLF, LFSpeed);

}


// GRAB UP

void grabUp(int speed) {
  analogWrite(motorFF, 0);
  analogWrite(motorFR, 0);
  delay(10);
  analogWrite(motorFF, speed);
  analogWrite(motorFR, 0);

}


// GRAB DOWN

void grabDown(int speed) {
  analogWrite(motorFF, 0);
  analogWrite(motorFR, 0);
  delay(10);
  analogWrite(motorFF, 0);
  analogWrite(motorFR, speed);

}

// GRAB STOP

void grabStop(int speed) {
  analogWrite(motorFF, 0);
  analogWrite(motorFR, 0);
  delay(10);

}

// Spin Left
void leftSpin(int speed) {
  analogWrite(motorRF, 0);
  analogWrite(motorRR, 0);
  analogWrite(motorLF, 0);
  analogWrite(motorLR, 0);
  delay(10);
  analogWrite(motorRF, speed);
  analogWrite(motorLR, speed);

}
// Spin Right
void rightSpin(int speed) {
  analogWrite(motorRF, 0);
  analogWrite(motorRR, 0);
  analogWrite(motorLF, 0);
  analogWrite(motorLR, 0);
  delay(10);
  analogWrite(motorRR, speed);
  analogWrite(motorLF, speed);

}
// Drive Reverse
void reverse(int speed) {
  analogWrite(motorRF, 0);
  analogWrite(motorRR, 0);
  analogWrite(motorLF, 0);
  analogWrite(motorLR, 0);
  delay(10);

  RRSpeed = LRSpeed = speed;
  analogWrite(motorRF, 0);
  analogWrite(motorRR, RRSpeed);
  analogWrite(motorLF, 0);
  analogWrite(motorLR, LRSpeed);

}
//Turn Right
void rightTurn(int speed) {
  analogWrite(motorRF, 0);
  analogWrite(motorRR, 0);
  analogWrite(motorLF, 0);
  analogWrite(motorLR, 0);
  delay(10);

  LFSpeed = speed;
  RFSpeed = speed / 2;
  analogWrite(motorRF, 0);
  analogWrite(motorRR, speed);
  analogWrite(motorLF, LFSpeed);
  analogWrite(motorLR, 0);

}
//Turn left
void leftTurn(int speed) {
  analogWrite(motorRF, 0);
  analogWrite(motorRR, 0);
  analogWrite(motorLF, 0);
  analogWrite(motorLR, 0);
  delay(10);

  RFSpeed = speed;
  LFSpeed = speed / 2;
  analogWrite(motorRF, RFSpeed);
  analogWrite(motorRR, 0);
  analogWrite(motorLF, LFSpeed);
  analogWrite(motorLR, 0);

}

//Stop
void stopCompletely() {
  analogWrite(motorRF, 0);
  analogWrite(motorRR, 0);
  analogWrite(motorLF, 0);
  analogWrite(motorLR, 0);
}

//================= SETUP ==================================
void setup() {


  //
  // ====== SERVO SETUP =============

  servo.attach(2);
  servo.write(angle);


  // ====== MOTOR SETUP =============
  pinMode(motorRF, OUTPUT);
  pinMode(motorRR, OUTPUT);
  pinMode(motorLF, OUTPUT);
  pinMode(motorLR, OUTPUT);
  Serial.begin(115200); // this tells the arduino in what baud to read the signal

  // ====== LIGHT SENSOR SETUP =============
  Serial.begin(9600);
  analogReference(INTERNAL);



}
//============= LOOP CODE=================

void loop() { //starts alternating motor movement for testing





  int touch = digitalRead(touchPin);
  int colour = analogRead(colourPin);
  Serial.print("touch:");
  Serial.println(touch);
  Serial.print("colour:");
  Serial.println(colour);
  delay(100);

  // == PRIMARY FEEDBACK IS FROM TOUCH SENSOR ======
  // if the robot touches a wall, simply reverse and turn around

  if (touch == 1) {
    //pull a u turn
    stopCompletely();
    delay(50);
    reverse(255);
    delay(250);
    leftSpin(255);
    delay(250);

    // if the colour shows up as less a digital read of 13, then that means the robot has run into black tape.
    // Begin grabber movement, then spin around and head a different direction
  } else if (colour < 13) {

    delay(1000);
    servo.write(90);
    delay(1000);
    servo.write(0);
    delay(1000);
    servo.write(90);
    delay(1000);
    servo.write(0);
    delay(1500);

    stopCompletely();
    delay(50);
    reverse(255);
    delay(250);
    rightSpin(250);
    delay(100);
  } else {

    // when all else fails, approach the arena in a stochastic fashion:
    // forward/right/left/reverse + move the servo up and down afterwards



    int whichway = random(1, 5);



    switch (whichway) {
      case 1: drive(255);
        delay(1500);
        servo.write(90);
        delay(1000);
        servo.write(0);
        delay(1000);
        break;
      case 2: rightSpin(255);
        delay(1000);
        drive(255);
        delay(1000);
        servo.write(90);
        delay(1000);
        servo.write(0);
        delay(1000);
        servo.write(90);
        delay(1000);
        servo.write(0);
        delay(1500);
        break;

      case 3: reverse(255);
        delay(1500);
      case 4: leftSpin(255);
        delay(1000);
        drive(255);
        delay(1500);
        break;
    }

  }
}
















