// point-to-multipoint transmit "Variation one"
#include <RadioLib.h>
SX1262 radio = new Module(D36, D40, D44, D39);

void setup() {
  Serial.begin(9600);
  
  Serial.print(F("[SX1262] Initializing ... "));
  int state = radio.begin(915.0, 250.0, 7, 5, 0x34, 20, 10, 0, false);;
  if (state == ERR_NONE) {
    Serial.println(F("success!"));
  } else {
    Serial.print(F("failed, code "));
    Serial.println(state);
    while (1);
  }
  

}

void loop() {
  Serial.print(F("[SX1262] Transmitting packet ... "));

   int state = radio.transmit("What's good?");

  if (state == ERR_NONE) {
    // the packet was successfully transmitted
    Serial.println(F("success!"));

    // print measured data rate
    Serial.print(F("[SX1262] Datarate:\t"));
    Serial.print(radio.getDataRate());
    Serial.println(F(" bps"));

  } else if (state == ERR_PACKET_TOO_LONG) {
    // the supplied packet was longer than 256 bytes
    Serial.println(F("too long!"));

  } else if (state == ERR_TX_TIMEOUT) {
    // timeout occured while transmitting packet
    Serial.println(F("timeout!"));

  } else {
    // some other error occurred
    Serial.print(F("failed, code "));
    Serial.println(state);

  }

  delay(1000); 

}
