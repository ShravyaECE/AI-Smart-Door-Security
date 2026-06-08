from flask import Flask, request
import numpy as np
import cv2
import face_recognition
import pickle
import os
from datetime import datetime

app = Flask(__name__)

# 🔹 Create folder
SAVE_DIR = "saved_images"
os.makedirs(SAVE_DIR, exist_ok=True)

# 🔹 Load encodings (LIST FORMAT)
with open("encodings.pkl", "rb") as f:
    known_encodings = pickle.load(f)

print("[INFO] Loaded encodings:", len(known_encodings))


# 🔹 Recognition
def recognize_face(frame):

    small = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    rgb = cv2.cvtColor(small, cv2.COLOR_BGR2RGB)

    boxes = face_recognition.face_locations(rgb, model="hog")

    # 🚨 No face
    if len(boxes) == 0:
        return "NO_FACE"

    encodings = face_recognition.face_encodings(rgb, boxes)

    for encoding in encodings:
        matches = face_recognition.compare_faces(
            known_encodings, encoding, tolerance=0.5
        )

        if True in matches:
            return "OPEN"

    return "CLOSE"


# 🔹 Save image
def save_image(frame, result):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    filename = f"{result}_{timestamp}.jpg"
    path = os.path.join(SAVE_DIR, filename)

    cv2.imwrite(path, frame)


# 🔹 API
@app.route("/upload", methods=["POST"])
def upload():

    if not request.data:
        return "NO_FACE"

    np_arr = np.frombuffer(request.data, np.uint8)
    frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    if frame is None:
        return "NO_FACE"

    result = recognize_face(frame)

    # 🔥 Always save
    save_image(frame, result)

    print("Result:", result)

    return result


# 🔹 RUN
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=False)