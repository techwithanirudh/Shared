#include <Servo.h>
Servo MyServoMotor1;

int Echo = 3;
int Trig = 4;

#define ENA 9
#define ENB 6
#define IN1 8
#define IN2 13
#define IN3 10
#define IN4 11
#define carSpeed 150
#define carSpeed2 150
int rightDistance = 0, leftDistance = 0;

void forward()
{
  analogWrite(ENA, carSpeed);
  analogWrite(ENB, carSpeed);
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, HIGH);
  Serial.println("Forward");
}

void back()
{
   analogWrite(ENA, carSpeed); 
   analogWrite(ENB, carSpeed);
   digitalWrite(IN1, LOW);
   digitalWrite(IN2, HIGH);
   digitalWrite(IN3, HIGH);
   digitalWrite(IN4, LOW);
   Serial.println("Back");
}

void left()
{
   analogWrite(ENA, carSpeed2); 
   analogWrite(ENB, carSpeed2);
   digitalWrite(IN1, LOW);
   digitalWrite(IN2, HIGH);
   digitalWrite(IN3, LOW);
   digitalWrite(IN4, HIGH);
   Serial.println("Left");
}

void right()
{
   analogWrite(ENA, carSpeed2); 
   analogWrite(ENB, carSpeed2);
   digitalWrite(IN1, HIGH);
   digitalWrite(IN2, LOW);
   digitalWrite(IN3, HIGH);
   digitalWrite(IN4, LOW);
   Serial.println("Right");
}

void stop()
{
   analogWrite(ENA, LOW); 
   analogWrite(ENB, LOW);
   Serial.println("Stop!")
}

long Distance_Test()
{
  pinMode(Trig, OUTPUT);  // Clear the trigger
  digitalWrite(Trig, LOW);
  delayMicroseconds(2);
  // Sets the trigger pin to HIGH state for 10 microseconds
  digitalWrite(Trig, HIGH);
  delayMicroseconds(10);
  digitalWrite(Trig, LOW);
  pinMode(Echo, INPUT);
  // Reads the echo pin, and returns the sound wave travel time in microseconds
  return pulseIn(Echo, HIGH);
}
void setup()
{
  MyServoMotor1.attach(5);
  Serial.begin(9600);
  pinMode(Echo, INPUT);
  pinMode(Trig, OUTPUT);
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);
  pinMode(ENA, OUTPUT);
  pinMode(ENB, OUTPUT);
  stop();
}

void loop()
{ 
     MyServoMotor1.write(60);
     delay(200);
     rightDistance = Distance_Test();
     MyServoMotor1.write(120);
     delay(200);
     leftDistance = Distance_Test();
     if ( (rightDistance > 70) && (leftDistance > 70) )
     {
      stop();
     }
     else if ( (rightDistance >= 20) && (leftDistance >= 20) )
     {
      forward();
      delay(100);
     }
     else if ( (rightDistance <= 10) && (leftDistance <= 10) )
     {
      back();
      delay(100);
     }
     else if (rightDistance - 3 > leftDistance)
     {
      left();
      delay(100);
     }
     else if (rightDistance + 3 < leftDistance)
     {
      right();
      delay(100);
     }
     else
     {
      stop();
     }
}
