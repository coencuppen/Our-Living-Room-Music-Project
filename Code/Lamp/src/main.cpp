#include <Arduino.h>
#include "Lamp.hpp"

Lamp lamp(A0, DD5);

void setup() {
    Serial.begin(9600);
}

void loop() {
    lamp.loop();
}