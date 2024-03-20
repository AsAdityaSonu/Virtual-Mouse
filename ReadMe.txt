### Hand Tracking Module

1. The script initializes a HandDetector class to manage hand tracking.
2. The findHands method detects hands in a frame.
3. The findPosition method extracts hand landmarks and bounding box.
4. The fingersUp method determines open or closed fingers.
5. The findDistance method calculates and visualizes distances.
6. The main function sets up video capture, processes frames, and displays the video stream.
7 .The application can be closed by pressing the 'q' key.

### Virtual Mouse

1. The script captures video from a webcam, detects hand gestures using the HandTrackingModule, and uses PyAutoGUI to control the cursor and perform clicks.
2. It includes logic to move the cursor when two fingers are open and click when the fingers are close together.
3. The frame rate (FPS) is calculated and displayed on the screen.
4. The application can be closed by pressing the 'q' key.