# 🎨 Air Canvas using OpenCV & MediaPipe

An interactive Computer Vision project that allows users to draw in the air using hand gestures captured through a webcam.

This project demonstrates real-time hand tracking and gesture recognition using OpenCV and MediaPipe.

---

## 🚀 Project Overview

The Air Canvas application enables users to draw virtually without touching the screen.
It tracks hand landmarks in real-time and uses specific finger gestures for interaction.

- ✌️ Two fingers (Index + Middle) are used for color selection mode.
- ☝️ One finger (Index finger) is used for drawing mode.

The system processes live video frames, detects hand landmarks using MediaPipe, and converts finger movements into smooth drawing strokes on a digital canvas.

---

## 🛠 Tech Stack

- Python
- OpenCV
- MediaPipe
- NumPy
- OOPs

---

## ✨ Features

- 🎨 Multiple color selection
- 🖐 Real-time hand landmark detection
- ✏ Smooth gesture-based drawing
- 🧽 Eraser functionality
- ⚡ Real-time video processing

---

## 🖥 How It Works

1. The webcam captures a continuous live video feed.
2. Each frame is processed and converted for hand detection.
3. MediaPipe identifies 21 hand landmarks in real time.
4. The positions of the Index and Middle fingertips are analyzed to determine the active mode:
   - Two fingers (Index + Middle) → Color Selection Mode
   - Single Index finger → Drawing Mode
5. The index fingertip coordinates are mapped to the canvas to render smooth drawing strokes dynamically.

---

