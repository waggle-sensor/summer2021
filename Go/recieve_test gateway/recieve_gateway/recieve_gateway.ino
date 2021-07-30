#include <SPI.h>
#include <LoRa.h>


void setup() {
  Serial.begin(9600);

  Serial.println("LoRa Reciever Gatway");
  // Pin defs for the SparkFun LoRa gateway- 1:
  // NSS = 16
  // DIO0 = 26
  // RST = 27

  LoRa.setPins(16, 27, 26);
  LoRa.setSignalBandwidth(250E3);
  LoRa.setSyncWord(0x34);
  LoRa.setPreambleLength(20);
  
  

  if (!LoRa.begin(915E6)) {
    Serial.println("Starting Reciever failed");
    while(1);
  }

}

void loop() {
  // try to parse packet
  int packetSize = LoRa.parsePacket();
  if (packetSize) {
    // received a packet
    Serial.print("Received packet '");

    // read packet
    while (LoRa.available()) {
      Serial.print((char)LoRa.read());
    }


    // print RSSI of packet
    Serial.print("' with RSSI ");
    Serial.println(LoRa.packetRssi());
  } else {
    Serial.println("not working lol");
  }
}
