import cv2
import face_recognition
import time
import numpy as np
from onvif import ONVIFCamera

def is_image_blurry(image, threshold=100):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    laplacian_var = cv2.Laplacian(gray, cv2.CV_64F).var()
    return laplacian_var < threshold

# Conectar à câmera ONVIF
def connect_to_onvif_camera(host, port, user, password):
    camera = ONVIFCamera(host, port, user, password)
    media_service = camera.create_media_service()
    profiles = media_service.GetProfiles()
    token = profiles[0].token
    stream_setup = {'StreamSetup': {'Stream': 'RTP-Unicast', 'Transport': {'Protocol': 'RTSP'}}, 'ProfileToken': token}
    uri = media_service.GetStreamUri(stream_setup)
    return uri.Uri

# Configurações da câmera IP ONVIF
host = '10.10.20.100'  # IP da câmera
port = 8000
user = 'admin'
password = 'gap35ds3'
stream_uri = connect_to_onvif_camera(host, port, user, password)

# Configurar OpenCV para ler o stream de vídeo
cap = cv2.VideoCapture(stream_uri)

pessoa_identificada = False
face_count = 0
known_faces_encodings = []
start_time = time.time()
count_interval = 10

while True:
    ret, frame = cap.read()
    if not ret:
        break

    if is_image_blurry(frame):
        if pessoa_identificada:
            print("Nenhuma pessoa identificada (imagem borrada)")
            pessoa_identificada = False
        continue

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    face_detected = False
    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_faces_encodings, face_encoding, tolerance=0.6)
        if not any(matches):
            known_faces_encodings.append(face_encoding)
            face_count += 1
            face_detected = True

    if face_detected:
        if not pessoa_identificada:
            print("Pessoa Identificada")
            pessoa_identificada = True
    else:
        if pessoa_identificada:
            print("Nenhuma pessoa identificada")
            pessoa_identificada = False

    for (top, right, bottom, left) in face_locations:
        cv2.rectangle(frame, (left, top), (right, bottom), (255, 0, 0), 2)

    cv2.imshow('Webcam', frame)

    current_time = time.time()
    if current_time - start_time >= count_interval:
        print(f"Rostos identificados no total: {face_count}")
        start_time = current_time

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
