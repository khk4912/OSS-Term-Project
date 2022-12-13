# OSS-Term-Project - Molcom Project

---
## Project motivation
To prevent others from getting caught doing other things on their computers at home or at work

---
## Project Summary
This project implements changing page if a face different from the registered face is recongnized.

---

## Installation

1. Clone the repository

```bash
git clone https://github.com/chance03/OSS-Term-Project.git
```

2. Install dependencies

```bash
cd OSS-Term-Project
pip install -r requirements.txt
```

## Usage

```bash
cd molcom
python main.py
```

---

### Demo Image

![image](https://user-images.githubusercontent.com/106923158/207044619-1ce8a668-6619-48a1-b876-82c113398caf.png)

- Left screen is the program. if you click 얼굴인식 box, Write the name of the person you want to register in English, and when your face approach to the camera, take 100 pictures of the person's face and save them in the program. If you click 시작 box, an object that is not registered on the camera is recognized, the computer's screen is switched
- right screen is git bash which is used to open the program.

---

### Demo Video

[Video](https://youtu.be/T2OjW052D-Y)

---

### Used Package

- opencv-python
- opencv-contrib-python
- pillow
- numpy
- pyautogui

---

### Reference

<http://velog.io/@huttzza/실시간-얼굴-인식-프로그램-1차-구현>

