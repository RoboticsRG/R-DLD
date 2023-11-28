#include <AccelStepper.h>
const int SPEED_MOTOR = 400;
const int ACCELERATION_MOTOR = 200;
const int PINO_ENABLE = 10; 

int input = 0;
AccelStepper motor1(1,7,4 ); 

void setup() {
  Serial.begin(9600);
  pinMode(PINO_ENABLE, OUTPUT);
  
  motor1.setMaxSpeed(SPEED_MOTOR);
  motor1.setSpeed(SPEED_MOTOR);
  motor1.setAcceleration(ACCELERATION_MOTOR);
  print_msg();

}

void print_msg() {
  Serial.println("Orientation:");
  Serial.println("0 - Portrait");
  Serial.println("1 - Landscape Left");
  Serial.println("2 - Landscape Right");
  Serial.println("3 - Upside Down");
}

void loop() {
  if (Serial.available() > 0)
  {
    input = Serial.read();
    if (input == '0')
    { 
      motor1.moveTo(0);     //Portrait
    }
    if (input == '1')
    {
      motor1.moveTo(50);    //Landscape Left
    }

    if (input == '2')
    {
      motor1.moveTo(100);   //Landscape Right
    }

    if (input == '3')
    {
      motor1.moveTo(150);   //Landscape Right
    }
    if (input == '4')
    {
      digitalWrite(PINO_ENABLE, HIGH);
    }
    if (input == '5')
    {
      digitalWrite(PINO_ENABLE, LOW);
    }
    if (input == '6')
    {
      motor1.moveTo(5000);
    }

  }

  

  motor1.run();

}
