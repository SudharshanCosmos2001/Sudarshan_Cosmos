// Transmitter

#include <Wire.h>
#include "Adafruit_BMP085.h"
#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

RF24 myRadio(7, 8); // CE, CSN

byte addresses[][6] = {"1Node"};

Adafruit_BMP085 altSensor;

struct pack{ 
 float tempC;
 float pressure;
}packet;


void setup() {
  // put your setup code here, to run once:
  myRadio.begin();
  myRadio.setChannel(108);
  myRadio.setPALevel(RF24_PA_MIN);
  myRadio.openWritingPipe(addresses[0]);
  
  altSensor.begin();
}

void loop() {
  // put your main code here, to run repeatedly:
  packet.tempC = altSensor.readTemperature();
  packet.pressure = altSensor.readPressure();
    
     myRadio.write(&packet, sizeof(packet));
     delay(500);
     
}
