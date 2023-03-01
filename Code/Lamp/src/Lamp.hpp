//
// Created by coenc on 01/03/2023.
//

#ifndef LAMP_LAMP_HPP
#define LAMP_LAMP_HPP

#include <Arduino.h>

class Lamp {
private:
    const unsigned int gatePin;
    const unsigned int signalReadPin;

public:
    Lamp(const unsigned int &gatePin, const unsigned int &signalRead);

    void loop() const;
};


#endif //LAMP_LAMP_HPP
