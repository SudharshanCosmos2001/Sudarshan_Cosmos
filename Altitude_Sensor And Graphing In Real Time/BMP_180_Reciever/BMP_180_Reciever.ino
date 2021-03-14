//Reciever

#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

RF24 myRadio(7, 8); // CE, CSN
 byte addresses[][6] = {"1Node"};

 struct Pack {
  float tempC;
  float pressure;
} packet;

void setup() {
  Serial.begin(115200);
  myRadio.begin();
  myRadio.setChannel(108);
  myRadio.setPALevel(RF24_PA_MIN);
  myRadio.openReadingPipe(1, addresses[0]);
  myRadio.startListening();
}

void loop() {
  if (myRadio.available()) {
    myRadio.read(&packet, sizeof(packet) );
    Serial.print(packet.tempC);
    Serial.print(" , ");
    Serial.println(packet.pressure);
      
 
    }
  }
