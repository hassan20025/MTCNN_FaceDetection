import cv2
import tensorflow as tf
from mtcnn import MTCNN

# Ensure TensorFlow uses GPU
if not tf.config.list_physical_devices('GPU'):
    print("Warning: No GPU found, using CPU instead.")
else:
    print("GPU is available, TensorFlow will use it.")

detector = MTCNN()

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # MTCNN will now use GPU if available
    faces = detector.detect_faces(frame)

    for face in faces:
        x, y, w, h = face['box']
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('MTCNN Face Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
