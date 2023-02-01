import cv2
import pyaudio
import numpy as np


class Microphone:
    def __init__(self, formatType, channels, rate, CHUNK, inputDevice):
        self.CHUNK = CHUNK
        self.stream = pyaudio.PyAudio().open(format=formatType, channels=channels, rate=rate, input=True,
                                             frames_per_buffer=CHUNK,
                                             input_device_index=inputDevice)  # input device op 1

    def getAmplitude(self):
        data = np.fromstring(self.stream.read(self.CHUNK), dtype=np.int16)
        counter = 1
        dataAverage = 0
        for j in range(len(data)):
            if data[j] > 0:
                dataAverage += data[j]
                counter += 1
        dataAverage /= counter
        return dataAverage


class Camera:
    def __init__(self, captureDevice):
        self.cap = cv2.VideoCapture(captureDevice + cv2.CAP_DSHOW)  # par should be 1
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)


class Window:
    def __init__(self, _camera, _mic, windowName, resize=(None, None)):
        self.camera = _camera
        self.mic = _mic
        self.windowName = windowName
        self.gauss = np.random.randn(HEIGHT, WIDTH, 3)
        self.newHeight = resize[0]
        self.newWidth = resize[1]
        self.loop()

    def Effect(self, frame):
        micValue = self.mic.getAmplitude().__int__()
        print(micValue)

        if micValue < 300:
            image = self.gauss - (micValue / 10)
        else:
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) - micValue / 10

        return image

    def loop(self):
        while True:
            _, frame = self.camera.cap.read()

            image = self.Effect(frame)

            if self.newHeight:
                image = cv2.resize(image, (self.newHeight, self.newWidth), cv2.INTER_NEAREST)

            cv2.imshow(self.windowName, image)

            if cv2.waitKey(1) & 0xFF == 27:
                cv2.destroyAllWindows()
                break


if __name__ == '__main__':
    WIDTH, HEIGHT = 240, 144  # resolution tv 1280x720
    camera = Camera(0)  # par should be 1
    mic = Microphone(pyaudio.paInt16, 1, 44100, 2 ** 10, 1)  # input device op 1
    window = Window(camera, mic, "Our Living Room Camera Feed", [1280, 720])
