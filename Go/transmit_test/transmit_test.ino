// Custom one-to-one transmission between two end node devices.
// By Lance Go

#include <RadioLib.h>

// SX1262 connections on the ExpLoRaBle board:
// NSS pin:   D36 // 19
// DIO1 pin:  D40 // 13
// NRST pin:  D44 // 15
// BUSY pin:  D39 // 14
// Definition of SPI1 in the module is necessary btw
SX1262 radio = new Module(D36, D40, D44, D39, SPI1);

byte byteArr[] = {0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x1, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x1, 0x01};


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  int state = radio.begin(915.0, 250.0, 7, 5, 0x34, 20, 10, 0, false);
  if (state == ERR_NONE) {
    Serial.println(F("done."));
  } else {
    Serial.println(F("failed, code: "));
    Serial.println(state);
    while(1);
  }
}

void loop() {
  // put your main code here, to run repeatedly:

  // test byte array to be transmitted:
  int state = radio.transmit(byteArr, 16);

  if (state == ERR_NONE){
    Serial.println(F("success!"));

    // print measured data rate
    Serial.print(F("[SX1262] Datarate:\t"));
    Serial.print(radio.getDataRate());
    Serial.println(F(" bps"));

    // alters data every successful transmit
    
  } else {
    Serial.print(F("Failure with code: "));
    Serial.println(state);
  }

  delay(200);

}
  

  
