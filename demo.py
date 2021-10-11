import cv2
import numpy as np

import mediapipe as mp
from mpx.face_landmark_with_geometry import FaceLandmarkFrontWithGeometry

mp_drawing = mp.solutions.drawing_utils
mp_face_mesh = mp.solutions.face_mesh

# For webcam input:
drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)
cap = cv2.VideoCapture("media/video-480.mov")

face_mesh = FaceLandmarkFrontWithGeometry()

while cap.isOpened():
    success, image = cap.read()
    if not success:
        print("Ignoring empty camera frame.")
        # If loading a video, use 'break' instead of 'continue'.
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue

    # Flip the image horizontally for a later selfie-view display, and convert
    # the BGR image to RGB.
    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    results = face_mesh.process(image)

    # Draw the face mesh annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            mp_drawing.draw_landmarks(
                image=image,
                landmark_list=face_landmarks,
                connections=mp_face_mesh.FACE_CONNECTIONS,
                landmark_drawing_spec=drawing_spec,
                connection_drawing_spec=drawing_spec)

    if results.multi_face_geometry:
        for i, geometry in enumerate(results.multi_face_geometry):
            raw_mat = geometry.pose_transform_matrix
            pose_mat = np.asarray(raw_mat.packed_data).reshape(raw_mat.cols, raw_mat.rows)
            h, w = image.shape[:2]

            p = np.asarray([0, 0, 0.2])
            pp = p.dot(pose_mat[:3, :3])

            center = results.multi_face_landmarks[i].landmark[1]

            x = (pp[0] + center.x) * w
            y = (-pp[1] + center.y) * h

            cv2.line(image, (round(center.x * w), round(center.y * h)),
                     (round(x), round(y)),
                     color=(255, 0, 255), thickness=2)

    cv2.imshow('MediaPipe FaceMesh', image)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cap.release()
