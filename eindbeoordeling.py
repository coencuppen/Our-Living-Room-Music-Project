import cv2
import numpy as np
import pyaudio
import time
import os

windowName = "Our Living Room Camera Feed"
WIDTH, HEIGHT = 1280, 720  # afmeting tv 1280x720
THRESHOLDSTART = 1000  # mic amplitude to start program
dTime = 1.9  # time (in s) to start the music

musicFile = "C:/Users/coenc/Documents/GitHub/Our-Living-Room-Music-Project/PythonCode/SAMENFINAL.wav"
niks = "C:/Users/coenc/Desktop/niks.mp3"
mrb = "C:/Users/coenc/Documents/GitHub/Our-Living-Room-Music-Project/PythonCode/mrbgrafiek.png"

deSpiraal = "C:/Users/coenc/Documents/GitHub/Our-Living-Room-Music-Project/PythonCode/despiraal.png"
goedWillendeGeestUitSiberie = "C:/Users/coenc/Documents/GitHub/Our-Living-Room-Music-Project/PythonCode/goedwilendegeestuitsiberie.png"
guldenSneede = "C:/Users/coenc/Documents/GitHub/Our-Living-Room-Music-Project/PythonCode/guldensneede.png"
hertEnVis = "C:/Users/coenc/Documents/GitHub/Our-Living-Room-Music-Project/PythonCode/hertenvis.png"
kabalahsterMetPaarden = "C:/Users/coenc/Documents/GitHub/Our-Living-Room-Music-Project/PythonCode/kabalahstermetpaarden.png"
levensLijn = "C:/Users/coenc/Documents/GitHub/Our-Living-Room-Music-Project/PythonCode/levenslijn.png"
motiefVanDeAlgonguin = "C:/Users/coenc/Documents/GitHub/Our-Living-Room-Music-Project/PythonCode/motiefvandealgonquin.png"
mystiekeLetters = "C:/Users/coenc/Documents/GitHub/Our-Living-Room-Music-Project/PythonCode/mystiekeletters.png"
octopus = "C:/Users/coenc/Documents/GitHub/Our-Living-Room-Music-Project/PythonCode/octopus.png"
siberischeTekening = "C:/Users/coenc/Documents/GitHub/Our-Living-Room-Music-Project/PythonCode/siberischetekening.png"
spiraal = "C:/Users/coenc/Documents/GitHub/Our-Living-Room-Music-Project/PythonCode/spiraal.png"
uil = "C:/Users/coenc/Documents/GitHub/Our-Living-Room-Music-Project/PythonCode/uil.png"
zeebra = "C:/Users/coenc/Documents/GitHub/Our-Living-Room-Music-Project/PythonCode/zeebra.png"
meltedFaces = "C:/Users/coenc/Documents/GitHub/Our-Living-Room-Music-Project/PythonCode/meltedfaces.png"
jor1 = "C:/Users/coenc/Documents/GitHub/Our-Living-Room-Music-Project/PythonCode/jor1.png"
jor2 = "C:/Users/coenc/Documents/GitHub/Our-Living-Room-Music-Project/PythonCode/jor2.png"
jor3 = "C:/Users/coenc/Documents/GitHub/Our-Living-Room-Music-Project/PythonCode/jor3.png"

#videoPath = "C:/Users/coenc/Documents/GitHub/Our-Living-Room-Music-Project/PythonCode/overgang1naar2convert.mp4"
#video = cv2.VideoCapture(videoPath)


images = [deSpiraal, goedWillendeGeestUitSiberie, guldenSneede, hertEnVis, kabalahsterMetPaarden, levensLijn,
          motiefVanDeAlgonguin, mystiekeLetters, octopus, siberischeTekening, spiraal, uil, zeebra]

imagesResized = []

for img in images:
    print(img)
    layer1 = cv2.resize(cv2.imread(img, cv2.IMREAD_UNCHANGED), (WIDTH, HEIGHT))

    for i in range(HEIGHT):
        for j in range(WIDTH):
            # print(img, " ", layer1[i][j])
            if layer1[i][j][3]:
                layer1[i][j][2] = 255

    imagesResized.append(layer1)

meltedFaces = cv2.resize(cv2.imread(meltedFaces, cv2.IMREAD_UNCHANGED), (WIDTH, HEIGHT))
jor1 = cv2.resize(cv2.imread(jor1, cv2.IMREAD_UNCHANGED), (WIDTH, HEIGHT))
jor2 = cv2.resize(cv2.imread(jor2, cv2.IMREAD_UNCHANGED), (WIDTH, HEIGHT))
jor3 = cv2.resize(cv2.imread(jor3, cv2.IMREAD_UNCHANGED), (WIDTH, HEIGHT))


font = cv2.FONT_HERSHEY_SIMPLEX
fontExcept = cv2.FONT_HERSHEY_PLAIN
counterLetters = 0
onOff = True
beatCounter = 0
letter = ['O', 'U', 'R', '~', 'H', 'O', 'U', 'S', 'E', '!', ]
sw = True
timeBy = 0
prevTime =0
imgCounter = 0

cap = cv2.VideoCapture(1 + cv2.CAP_DSHOW)  # par should be 1
cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)

cell_width, cell_height = 12, 12
new_width, new_height = int(WIDTH / cell_width), int(HEIGHT / cell_height)

audio = pyaudio.PyAudio()
CHUNK = 2 ** 10  # Block Size
stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True,
                    frames_per_buffer=CHUNK, input_device_index=1)  # input device op 1


def effect(image, scene, letter):
    global black_window, boem, musicSwitch, fadeInValue, onOff, cap

    black_window = np.zeros((HEIGHT, WIDTH, 3), np.uint8)

    small_image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_NEAREST)

    if scene == 1:
        black_window = cv2.Canny(frame, fadeInValue, fadeInValue)
        cv2.putText(black_window, measureAmplitude().__str__(), (100, 600), font, 1,
                    (fadeIn(0.7), fadeInValue, fadeInValue), 3, cv2.LINE_8)
        return

    if scene == 2:
        black_window = cv2.Canny(frame, fadeInValue, fadeInValue)
        cv2.putText(black_window, measureAmplitude().__str__(), (200, 600), font, 1,
                    (fadeIn(0.7), fadeInValue, fadeInValue), 3, cv2.LINE_8)
        cv2.putText(black_window, "IK BEN NOG NIET VAN MIJ HOE KAN IK DAN VAN JOU ZIJN", (100, 100), font, 1,
                    (255, 0, 0), 1, cv2.LINE_8)
        return

    if scene == None:
        fadeOut(10)

    if scene == 6:
        beatCounter()
        if onOff:
            black_window = cv2.Canny(frame, measureAmplitude(), measureAmplitude())
        else:
            cv2.imshow(windowName, imagesResized[0])

    if scene == 7:
        cv2.putText(black_window, 'EXCEPT', (30, 390), fontExcept, 20, (0, 0, fadeOut(0.3)), 25, cv2.LINE_AA)

    if scene == 8:
        cv2.putText(black_window, 'ACCEPT', (30, 390), fontExcept, 20, (0, 0, 255), 25, cv2.LINE_AA)

    if scene == 9:
        beatCounter(150)
        ampl = measureAmplitude().__int__() % 255
        if onOff:
            cv2.putText(black_window, 'EXCEPT', (30, 390), fontExcept, 20, (ampl, ampl, 0 ), 25, cv2.LINE_AA)
        else:
            cv2.putText(black_window, 'ACCEPT', (30, 390), fontExcept, 20, (ampl, 0, ampl), 25, cv2.LINE_AA)

    if scene == 4 or scene == 5 or scene == 13:
        measure = measureAmplitude().__int__()
    for i in range(new_height):
        for j in range(new_width):
            color = small_image[i, j]
            B = int(color[0])
            G = int(color[1])
            R = int(color[2])

            coord = (j * cell_width + cell_width, i * cell_height)

            if scene == 0:
                cv2.putText(black_window, 'OUR LIVING ROOM', (coord[0] * 30 - 230, coord[1] * 5 - 5), font, 1,
                            (B, G, R), 1, cv2.LINE_AA)

            if scene == None:
                cv2.putText(black_window, 'OUR LIVING ROOM', (coord[0] * 30 - 230, coord[1] * 5 - 5), font, 1,
                            (fadeOutValue, fadeOutValue, fadeOutValue), 1, cv2.LINE_AA)


            # cv2.circle(black_window, coord, 5, (0, G, 0), 2)

            # cv2.circle(black_window, coord, 5, (0, G, 0), -1)
            if scene == 5:
                cv2.circle(black_window, coord, 5 + measure % 5, (B, G, R), -1)

            if scene == 13:
                coord = (j * cell_width + cell_width, i * cell_height + measureAmplitude().__int__())
                cv2.circle(black_window, coord, 5 + measure/5, (B, G, R), -1)

            # cv2.line(black_window, coord, (coord[0] + 8, coord[1]), (0, G, 0), 1)
            if scene == 4:
                cv2.line(black_window, (coord[0] + 4 + fadeIn(), coord[1] - 4), (coord[0] + 4, coord[1] + 4), (0, G, measure*2),1)



                #cv2.putText(black_window, '69', (coord[0] * 10 - 230, coord[1]), font, 1,
                #            (fadeOutValue, fadeOutValue, fadeOutValue), 1, cv2.LINE_AA)


def beatCounter(bpm=0.46115, counter = False):
    global onOff, timeBy, prevTime, imgCounter

    if timeBy > prevTime + (1 / (bpm / 60)):
        prevTime = timeBy
        onOff = not onOff
        if counter:
            imgCounter += 1
            if imgCounter > len(imagesResized) -1:
                imgCounter = 0

    return imgCounter



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


fadeInValue = 0


def fadeIn(delta =1):
    global fadeInValue
    fadeInValue += delta
    # print(fadeInValue)
    return fadeInValue


fadeOutValue = 255


def fadeOut(delta=1):
    global fadeOutValue
    if fadeOutValue > 0:
        fadeOutValue -= delta
        if fadeOutValue < 0:
            fadeOutValue = 0
    return fadeOutValue


def checkScene():
    global timeBegin, fadeInValue, fadeOutValue, timeBy
    timeBy = time.time() - timeBegin
    # print(timeBy)

    if timeBy > 498:
        return 13
    if timeBy > 455:
        return 12
    if timeBy > 368:
        fadeInValue = 0
        return 11
    if timeBy > 289:
        fadeOutValue = 255
        return 10
    if timeBy > 277:
        return 9
    if timeBy > 199:
        return 8
    if timeBy > 118:
        return 7
    if timeBy > 85:
        return 6
    if timeBy > 70:
        fadeOutValue = 255
        return 5
    if timeBy > 57:
        return 4
    if timeBy > 47:
        fadeInValue =0
        return 3
    if timeBy > 27:
        return 2
    if timeBy > 4:
        return 1


def waitStart():
    global musicSwitch
    while True:
        _, frame = cap.read()
        effect(frame, 0, letter[counterLetters])
        cv2.imshow(windowName, black_window)
        if cv2.waitKey(1) & 0xFF == 27:
            cv2.destroyAllWindows()
            exit()
        if measureAmplitude() > THRESHOLDSTART:
            break
    os.system(musicFile)


waitStart()
timeBegin = time.time() + dTime

while True:
    beatCounter()
    scene = checkScene()
    _, frame = cap.read()

    effect(frame, scene, letter[counterLetters])

    cv2.imshow(windowName, black_window)

    if scene == 10:
        cv2.imshow(windowName, imagesResized[beatCounter(150, True)])

    if scene == 11:
        cv2.imshow(windowName, meltedFaces)

    if scene == 12:
        beatCounter(100)
        if onOff:
            cv2.imshow(windowName, meltedFaces)
        else:
            cv2.imshow(windowName, cv2.Canny(meltedFaces, fadeIn(2), fadeInValue))

    if cv2.waitKey(1) & 0xFF == 27:
        # os.system(niks)
        break

cv2.destroyAllWindows()
