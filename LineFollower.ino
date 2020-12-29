#define LeftSensor 12
#define RightSensor 13
#define LeftMotor1 8 
#define LeftMotor2 9
#define RightMotor1 10 
#define RightMotor2 11
 
void setup() {
  Serial.begin(9600);
  pinMode(LeftSensor, INPUT);
  pinMode(RightSensor, INPUT);

  pinMode(LeftMotor1, OUTPUT);
  pinMode(LeftMotor2, OUTPUT);
  pinMode(RightMotor1, OUTPUT);
  pinMode(RightMotor2, OUTPUT);
}

void loop() {
  Serial.println(digitalRead(LeftSensor));
  Serial.println(digitalRead(RightSensor));
  delay(500);
  if (!(digitalRead(LeftSensor)) && digitalRead(RightSensor))
  {
     digitalWrite(LeftMotor1, LOW);
     digitalWrite(LeftMotor2, LOW);
     digitalWrite(RightMotor1, HIGH);
     digitalWrite(RightMotor2, LOW);
     Serial.println("RIGHT");
  }
  if (!(digitalRead(RightSensor)) && digitalRead(LeftSensor))
  {
     digitalWrite(LeftMotor1, HIGH);
     digitalWrite(LeftMotor2, LOW);
     digitalWrite(RightMotor1, LOW);
     digitalWrite(RightMotor2, LOW);
     Serial.println("LEFT");
  }
  if (digitalRead(RightSensor) && digitalRead(LeftSensor))
  {
     digitalWrite(LeftMotor1, LOW);
     digitalWrite(LeftMotor2, HIGH);
     digitalWrite(RightMotor1, LOW);
     digitalWrite(RightMotor2, HIGH);
     Serial.println("FORWARD");
  }
  if (!(digitalRead(RightSensor)) && !(digitalRead(LeftSensor)))
  {
     digitalWrite(LeftMotor1, LOW);
     digitalWrite(LeftMotor2, LOW);
     digitalWrite(RightMotor1, LOW);
     digitalWrite(RightMotor2, LOW);
     Serial.println("STOP");
  }
}
