import cv2
import mediapipe as mp
import time
import math
import numpy as np


def main():
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        # FPS on screen
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(frame, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 255), 3)

        # Displaying Video
        cv2.imshow("frame", frame)
        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()  # Release the video capture object
    cv2.destroyAllWindows()  # Close all OpenCV windows


if __name__ == "__main__":
    main()
