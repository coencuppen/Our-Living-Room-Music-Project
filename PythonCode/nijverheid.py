import cv2
import pyaudio
import numpy as np
import random
import os
from PIL import Image, ImageFilter


font = cv2.FONT_HERSHEY_SIMPLEX
windowName = "Our Living Room Camera Feed"
WIDTH, HEIGHT = 1280, 720  # afmeting tv 1280x720
THRESHOLDSTART = 1000  # mic amplitude to start program

cap = cv2.VideoCapture(0 + cv2.CAP_DSHOW)  # par should be 1
cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)

audio = pyaudio.PyAudio()
CHUNK = 2 ** 10  # Block Size
stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True,
                    frames_per_buffer=CHUNK, input_device_index=1)  # input device op 1

row, col, ch = HEIGHT, WIDTH, 3
gauss = np.random.randn(row, col, ch)

def noisy(image, amount = 0):

    #gauss = gauss.reshape(row, col, ch)

    micValue = measureAmplitude().__int__()
    print(micValue)
    if micValue > 200:
        micValue = 200
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    #noisy = ((gauss - micValue) + (image + micValue)) / micValue

    if micValue < 100:
        noisy = gauss - (micValue/4)
    else:
        noisy = image - (micValue)


    #print(micValue)
    #noisy = cv2.cvtColor(noisy, cv2.COLOR_BGR2GRAY)
    return noisy


def measureAmplitude():
    data = np.fromstring(stream.read(CHUNK), dtype=np.int16)
    counter = 1
    dataAverage = 0
    for j in range(len(data)):
        if data[j] > 0:
            dataAverage += data[j]
            counter += 1
    dataAverage /= counter
    # print(dataAverage)
    return dataAverage


while True:
    _, frame = cap.read()

    #cv2.putText(frame, measureAmplitude().__str__(), (200, 600), font, 1,
    #            (255, 255, 255), 3, cv2.LINE_8)

    cv2.imshow(windowName, noisy(frame, measureAmplitude()))

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
