#include <Servo.h>
Servo MyServoMotor1;
void setup()
{
  MyServoMotor1.attach(5);
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);
  Serial.begin(9600);
}

long readUltrasonicDistance(int triggerPin, int echoPin)
{
  pinMode(triggerPin, OUTPUT);  // Clear the trigger
  digitalWrite(triggerPin, LOW);
  delayMicroseconds(2);
  // Sets the trigger pin to HIGH state for 10 microseconds
  digitalWrite(triggerPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(triggerPin, LOW);
  pinMode(echoPin, INPUT);
  // Reads the echo pin, and returns the sound wave travel time in microseconds
  return pulseIn(echoPin, HIGH);
}

void loop()
{
   int i=0;
   for (i=0; i<180; i++)
   {
     MyServoMotor1.write(i);
     int val = 0.01723 * readUltrasonicDistance(4, 3);
     Serial.println(val);
     delay(10);
   }
   for (i=180; i>0; i--)
   {
     MyServoMotor1.write(i);
     int val = 0.01723 * readUltrasonicDistance(4, 3);
     Serial.println(val);
     delay(10);
   }  
}
