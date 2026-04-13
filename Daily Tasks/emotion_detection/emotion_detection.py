import cv2
import numpy as np
import tensorflow as tf
from tensorflow import keras

model = tf.keras.models.load_model(
    r"C:\Users\QorxmazShahbazli\Downloads\emotions_predictions (3).keras"
)
emotion_labels = ['Angry', 'Happy', 'Neutral', 'Sad', 'Suprise']

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)


if not cap.isOpened():
    print('Cannot open camera')

while True:
    ret, frame = cap.read()

    if not ret:
        print('Cant recieve frame')
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 5)

    for (x, y, w, h) in faces:
        # crop from the original frame
        face_color = frame[y:y+h, x:x+h] #still BGR

        face_rgb = cv2.cvtColor(face_color, cv2.COLOR_BGR2RGB)

        face_resized = cv2.resize(face_rgb, (224, 224))


        face_input = np.expand_dims(face_resized, axis = 0)
        predictionns = model.predict(face_input)
        emotion_index = np.argmax(predictionns)
        emotion = emotion_labels[emotion_index]


        cv2.rectangle(frame, (x, y), (x + w, y+h), (255, 0, 0), 2)
        cv2.putText(frame, emotion, (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    cv2.imshow('webcam feed', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()