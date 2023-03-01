//
// Created by coenc on 01/03/2023.
//

#include "Lamp.hpp"

Lamp::Lamp(const unsigned int &gatePin, const unsigned int &signalRead) : gatePin(gatePin),
                                                                          signalReadPin(signalRead) {}

void Lamp::loop() const {
    const int signal = analogRead(signalReadPin); // analogRead goes from 0 to 1024
    analogWrite(gatePin, signal / 4); // analogWrite goes from 0 to 255
}