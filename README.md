# AI Smart Door Security System

## Overview
An AI-powered smart door security system that uses facial recognition to identify authorized users and control door access.

## Features
- Face Detection
- Face Recognition
- Authorized User Access
- Intruder Detection
- IoT-Based Door Control

## Hardware Used
- ESP32
- Camera Module
- Servo Motor
- Power Supply

## Software Used
- Python
- OpenCV
- Face Recognition Library
- Arduino IDE

## Working
1. Camera captures visitor image.
2. AI model detects and recognizes the face.
3. If authorized, the door unlocks automatically.
4. If unauthorized, access is denied.

## Future Improvements
- Mobile App Integration
- Cloud Database
- Visitor Logging

## Technologies Used
- Python
- OpenCV
- Face Recognition
- ESP32
- Arduino IDE
- IoT

## Working
1. Camera captures the visitor's face.
2. Face recognition identifies the person.
3. If the face matches an authorized user, the door unlocks.
4. If the face is unknown, access is denied.
5. The system can notify the owner about unauthorized access.

## Project Results

### Authorized User Detection
![Authorized](AI-Smart-Door-Security/authorized/authorized 1.webp)

### Unauthorized User Detection
![Unauthorized](AI-Smart-Door-Security/unauthorized/unauthorized 2.webp)


## How to Run

1. Install dependencies
```bash
pip install -r requirements.txt
python train_model.py
python encode_faces.py

3.project architecture
Workflow:

Camera → Face Detection → Face Recognition → Access Decision → Door Unlock/Access Denied


## Author
Ch.Shravya
B.Tech ECE | KITSW
