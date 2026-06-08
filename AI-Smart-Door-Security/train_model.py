import os
import cv2
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import joblib

# ================= PATH =================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET_PATH = os.path.join(BASE_DIR, "dataset")

AUTH_PATH = os.path.join(DATASET_PATH, "authorized")
UNAUTH_PATH = os.path.join(DATASET_PATH, "unauthorized")

# ================= LOAD DATA =================
data = []
labels = []

def load_images(folder, label):
    for file in os.listdir(folder):
        path = os.path.join(folder, file)
        img = cv2.imread(path)

        if img is None:
            continue

        img = cv2.resize(img, (64, 64))
        img = img.flatten()

        data.append(img)
        labels.append(label)

# Load both classes
load_images(AUTH_PATH, 1)   # authorized = 1
load_images(UNAUTH_PATH, 0) # unauthorized = 0

data = np.array(data)
labels = np.array(labels)

print("Data loaded:", data.shape)

# ================= TRAIN =================
X_train, X_test, y_train, y_test = train_test_split(
    data, labels, test_size=0.2, random_state=42
)

model = SVC(kernel='linear', probability=True)
model.fit(X_train, y_train)

# ================= ACCURACY =================
accuracy = model.score(X_test, y_test)
print("Model Accuracy:", accuracy)

# ================= SAVE MODEL =================
model_path = os.path.join(BASE_DIR, "model.pkl")
joblib.dump(model, model_path)

print("✅ Model saved at:", model_path)