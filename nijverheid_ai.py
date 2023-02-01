import cv2
import numpy as np
windowName = "Our Living Room Camera Feed"
WIDTH, HEIGHT = 1280, 720  # afmeting tv 1280x720
def display_webcam_with_noise(noise_level):
    # Open webcam
    cap = cv2.VideoCapture(0 + cv2.CAP_DSHOW)  # par should be 1
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Add black and white noise
        rows, cols, channels = frame.shape
        gauss = np.random.randn(rows, cols, channels)
        gauss = gauss.reshape(rows, cols)
        frame = frame + (gauss * noise_level)

        # Display the resulting frame
        cv2.imshow('Webcam', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

# Example usage:
display_webcam_with_noise(0) # this will add 50% noise to webcam feed