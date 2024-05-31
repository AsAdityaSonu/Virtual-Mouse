import cv2


# Main Function
def main():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()

        cv2.imshow("Video", frame)
        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
