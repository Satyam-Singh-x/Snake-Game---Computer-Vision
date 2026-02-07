🐍 Hand-Controlled Snake Game using OpenCV & MediaPipe



A modern twist on the classic Snake Game, controlled entirely by your hand gestures in real time using computer vision.

No keyboard. No mouse. Just ✋ + 🧠 + Python.


🚀 Overview

This project uses OpenCV, MediaPipe hand tracking, and CVZone to let you control a snake with your index finger captured via webcam.

The snake follows your finger smoothly, eats food, grows longer, and ends the game if it collides with itself.

Built as a computer vision + interactive gaming project, this is perfect for showcasing:

Real-time vision pipelines

Gesture-based control

Game logic & state management



✨ Features

🎥 Real-time webcam input

✋ Hand tracking with MediaPipe

👉 Index finger–controlled snake movement

🍩 Food spawning & score tracking

📈 Dynamic snake growth

💥 Self-collision detection

🔄 Instant restart (Press R)

🧠 Smooth motion using distance-based length control

🛠️ Tech Stack

Python

OpenCV

MediaPipe

CVZone

NumPy

📂 Project Structure

Snake Game/
│
├── snake_game.py            # Main game logic

├── HandTrackingModule.py    # MediaPipe hand detector

├── donut.png                # Food image (PNG with transparency)

├── snake_transparent.png    # Snake head image

└── README.md



▶️ How It Works

Webcam captures live video feed

MediaPipe detects hand landmarks

Index finger tip (Landmark 8) controls snake head

Snake body grows as it eats food

Collision with itself → Game Over



🎮 Controls

Action	Control

Move Snake	Move your index finger

Restart Game	Press R

Exit	Press ESC



⚙️ Installation


pip install opencv-python mediapipe cvzone numpy


⚠️ Recommended MediaPipe version

pip install mediapipe==0.10.9



🧠 Learning Outcomes

Real-time computer vision pipelines

MediaPipe hand landmark extraction

Game physics using distance accumulation

Collision detection with contours

Clean separation of vision & game logic

📸 Demo

https://youtu.be/ic80-0msJJk?si=0TxQJHY1Tin3yB96





🌟 Why This Project Matters


This is more than a game — it demonstrates:

Practical use of AI + CV

Real-time system performance

Interactive UI without traditional inputs

Perfect for ML / CV portfolios, hackathons, or just having fun with computer vision.




🤝 Contributing

Feel free to fork, improve, or add:

Gesture-based pause

Difficulty levels

Sound effects

Multiplayer mode 👀

PRs are welcome!

📜 License

MIT License — free to use, learn from, and build upon.

Made with love-
Satyam
