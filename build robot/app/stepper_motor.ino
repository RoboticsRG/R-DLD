#include <AccelStepper.h>
const int VELOCIDADE_MOTOR = 400;
const int ACELERACAO_MOTOR = 200;
const int PINO_ENABLE = 10; // Definicao pino ENABLE

int input = 0;
AccelStepper motor1(1,7,4 ); // Definicao pinos STEP e DIR

void setup() {
  Serial.begin(9600);
  pinMode(PINO_ENABLE, OUTPUT);
  // Configuracoes iniciais motor de passo
  motor1.setMaxSpeed(VELOCIDADE_MOTOR);
  motor1.setSpeed(VELOCIDADE_MOTOR);
  motor1.setAcceleration(ACELERACAO_MOTOR);
  print_msg();

}

void print_msg() {
  Serial.println("Digite:");
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
      motor1.moveTo(0);     //orientacao retrato
    }
    if (input == '1')
    {
      motor1.moveTo(50);    //orientacao paisagem esquerda
    }

    if (input == '2')
    {
      motor1.moveTo(100);   //orientacao retrato invertido 
    }

    if (input == '3')
    {
      motor1.moveTo(150);   //orientacao paisagem direita
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
