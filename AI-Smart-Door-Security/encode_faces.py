import face_recognition
import os
import pickle

dataset_path = "dataset/authorized"

encodings = []

for file in os.listdir(dataset_path):
    path = os.path.join(dataset_path, file)

    image = face_recognition.load_image_file(path)
    faces = face_recognition.face_encodings(image)

    if len(faces) > 0:
        encodings.append(faces[0])

with open("encodings.pkl", "wb") as f:
    pickle.dump(encodings, f)

print("✅ Encodings saved successfully")