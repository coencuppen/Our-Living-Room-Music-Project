import cv2
import numpy as np
import pyaudio

windowName = "Our House Camera Feed"
cap = cv2.VideoCapture(0 + cv2.CAP_DSHOW)

WIDTH, HEIGHT = 800, 600
cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)

cell_width, cell_height = 12, 12
new_width, new_height = int(WIDTH / cell_width), int(HEIGHT / cell_height)

font = cv2.FONT_HERSHEY_SIMPLEX

audio = pyaudio.PyAudio()
FORMAT = pyaudio.paInt16 # data type formate
CHANNELS = 1 # Adjust to your number of channels
RATE = 44100 # Sample Rate
CHUNK = 1024 # Block Size
stream = audio.open(format=FORMAT, channels=CHANNELS,
                rate=RATE, input=True,
                frames_per_buffer=CHUNK)

def effect(image, onOFF, letter):
    global black_window

    black_window = np.zeros((HEIGHT, WIDTH, 3), np.uint8)

    small_image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_NEAREST)

    for i in range(new_height):
        for j in range(new_width):
            color = small_image[i, j]
            B = int(color[0])
            G = int(color[1])
            R = int(color[2])

            coord = (j * cell_width + cell_width, i * cell_height)

            #cv2.circle(black_window, coord, 5, (B, G, R), 2)
            # cv2.circle(black_window, coord, 5, (0, G, 0), 2)
            # cv2.circle(black_window, coord, 5, (0, G, 0), -1)
            # cv2.circle(black_window, coord, 5, (B, G, R), -1)

            # cv2.line(black_window, coord, (coord[0] + 8, coord[1]), (0, G, 0), 1)
            # cv2.line(black_window, (coord[0] + 4, coord[1] - 4), (coord[0] + 4, coord[1] + 4), (0, G, 0), 1)
            if onOFF:
                cv2.putText(black_window, letter, coord, font, 0.4, (B, G, R), 1, cv2.LINE_AA)
            else:
                cv2.putText(black_window, letter, coord, font, 0.4, (0, G, 0), 1, cv2.LINE_AA)

counter = 0
counterLetters = 0
onOff = True
letter = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

while True:

    print(stream.read(CHUNK))
    _, frame = cap.read()
    if counter == 5:
        counterLetters += 1
        if counterLetters == 26:
            counterLetters = 0

    if counter == 10:
        counter = 0
        onOff = not onOff

    effect(frame, onOff, letter[counterLetters])
    counter+=1

    cv2.imshow(windowName, black_window)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()