📸 Hand Gesture Zoom Control using MediaPipe and OpenCV

This project allows you to control zoom functionality on your computer using hand gestures via webcam. It uses MediaPipe to detect the distance between your thumb and index finger, and simulates zoom in/out based on that distance using pyautogui.
🚀 Features

    Real-time hand tracking using MediaPipe

    Calculates distance between thumb and index finger

    Smooth zoom control using Ctrl + = and Ctrl + - hotkeys

    Adjustable sensitivity and scaling

    Works on any system-level zoom-supported app (browser, IDE, etc.)

🔧 Installation
✅ Install Required Packages

Make sure Python is installed. Then, install the dependencies:

pip install opencv-python mediapipe numpy pyautogui

▶️ Usage

    Clone the repository:

git clone https://github.com/your-username/hand-gesture-zoom.git
cd hand-gesture-zoom

    Run the script:

python hand_zoom.py

    Show your hand to the webcam and use your thumb and index finger to zoom:

        Move fingers apart ➝ Zoom In

        Move fingers closer ➝ Zoom Out

    Press q to exit the application.

🧠 How It Works

    The webcam captures the video stream.

    MediaPipe tracks hand landmarks.

    Distance between thumb tip and index finger tip is calculated.

    Based on the change in distance, Ctrl + = or Ctrl + - is triggered using pyautogui.

📌 Notes

    This app uses screen-level hotkeys, so ensure the target app (like a browser or PDF reader) supports Ctrl + zooming.

    Works best with a clear background and good lighting.

    Currently supports only one hand for gesture control.

👨‍💻 Author

Made by Sreyas P 🦇
Feel free to contribute or raise issues.
📜 License

MIT License – do whatever you want 🤘
