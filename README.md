Invisible Cloak Project 🧙‍♂️✨
📌 Project Overview

A fun Python + OpenCV project that creates an invisibility cloak effect.
This project detects a specific color in the video (like a red object) and makes it appear invisible by replacing it with the background in real-time.

It's a simple example of computer vision using color detection and masking.

---

## 🧰 Tech Stack
- Python 3.x  
- OpenCV (`cv2`)  
- NumPy  
- Webcam (for live video input)

---

## 📂 Project Structure

InvisibleCloak/
├── background.py # Captures and processes the background
├── invisible.py # Main script for invisibility effect
├── invisible_cloak.py # Alternative implementation
├── invisible_clock.py # Clock version (optional fun variant)
└── README.md # This file

## ▶️ How to Run

1. Clone the repository:
```bash
git clone https://github.com/Madhavi-1234/Invisible_Cloak.git

2.Navigate into the repo folder:

cd Invisible_Cloak


3. Install required libraries:

  pip install opencv-python numpy


4. Run the main script:

python invisible.py


5.Hold a cloth of the chosen color in front of the camera to see the invisibility effect.


📝 How It Works

Capture the background frame (without the cloak)

Detect the cloak color in each frame using color thresholding

Replace cloak area with background using masking

Show the final video output in real-time
