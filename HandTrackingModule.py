# Import Libraries
import cv2
import time
import mediapipe as mp

# Initializing the Model
mpHands = mp.solutions.hands
hands = mpHands.Hands(
    static_image_mode=False,
    model_complexity=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7,
    max_num_hands=1,
)


# Main Function
def main():
    cap = cv2.VideoCapture(0)
    draw = mp.solutions.drawing_utils   # Drawing Utilities
    while True:
        ret, frame = cap.read()
        frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        processed = hands.process(frameRGB)

        # Draw the Hand Landmarks
        landmarks_list = []
        if processed.multi_hand_landmarks:
            for hand_landmarks in processed.multi_hand_landmarks:
                draw.draw_landmarks(frame, hand_landmarks, mpHands.HAND_CONNECTIONS)
                for lm in hand_landmarks.landmark:
                    h, w, c = frame.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    landmarks_list.append([cx, cy])

            print(landmarks_list)

        cv2.flip(frame, 1)
        cv2.imshow("Video", frame)
        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
