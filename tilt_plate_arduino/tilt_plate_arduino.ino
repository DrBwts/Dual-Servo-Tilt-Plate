#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();

int pwm_val;
int servo = 1;
int i = 0;

void setup() {
  Serial.begin(9600);

  pwm.begin();
  pwm.setPWMFreq(60);  // Analog servos run at ~60 Hz updates

  pwm.setPWM(0, 0, 359);
  pwm.setPWM(1, 0, 359); // 359 ~centre

  delay(10);
}


void loop() 
{
  // Un/comment if using serial 
  //    first byte - start byte
  //    second byte - servo number
  //    third byte - servo position in degrees (0 - 180) 
  // if (Serial.available() > 2) {  
    
  //   start_byte = Serial.read();
  //   if (start_byte == 255) {
  //     for (i=0;i<2;i++) {
  //       user_input[i] = Serial.read();
  //     }
  //     servo   = user_input[0];
  //     pwm_val = map(user_input[1], 0, 180, 140, 500);
  //     pwm.setPWM(servo, 0, pwm_val);
  //   }
  // }

  // Centres servos - un/comment out as needed
  // i = 127;
  // pwm_val = map(i, 0, 255, 120, 600);
  // pwm.setPWM(0, 0, pwm_val);
  // pwm.setPWM(1, 0, pwm_val); 

  // Serial.println(pwm_val);

  // Un/comment for full sweeps of both servos one at a time
//  for( int i = 0; i < 200; i++ ){
//     pwm_val = map(i, 0, 255, 120, 600);
//     pwm.setPWM(servo, 0, pwm_val);
//     Serial.println(i);
//     Serial.println(pwm_val);
//     if (i == 127){
//      Serial.println("here");
//     }
    // delay(300);
//  }
//
//  for( int i = 200; i > 0; i-- ){
//     pwm_val = map(i, 0, 255, 120, 600);
//     pwm.setPWM(servo, 0, pwm_val);
//     Serial.println(i);
//     Serial.println(pwm_val);
//     if (i == 127){
//      Serial.println("here");
//     }
//     delay(300);
//  }
}
