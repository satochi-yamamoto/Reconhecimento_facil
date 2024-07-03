import cv2
import face_recognition
import datetime
from onvif import ONVIFCamera

# Configurações da câmera
cam_ip = 'IP_DA_CAMERA'
cam_port = 80  # Porta padrão
cam_user = 'USUARIO'
cam_pass = 'SENHA'

# Conectar à câmera
mycam = ONVIFCamera(cam_ip, cam_port, cam_user, cam_pass)
media_service = mycam.create_media_service()
stream_uri = media_service.GetStreamUri({'StreamSetup': {'Stream': 'RTP-Unicast', 'Transport': 'UDP'}, 'ProfileToken': 'PROFILE_TOKEN'})
stream_url = stream_uri.Uri

# Inicializa a captura de vídeo
cap = cv2.VideoCapture(stream_url)

# Lista para armazenar rostos conhecidos
known_face_encodings = []
known_face_names = []

# Dicionário para contagem de detecções
face_counter = {}

# Função para salvar log
def save_log(face_id, timestamp):
    with open("face_log.txt", "a") as log_file:
        log_file.write(f"Pessoa {face_id}, Data/Hora: {timestamp}\n")

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Converte a imagem BGR para RGB
    rgb_frame = frame[:, :, ::-1]

    # Localiza todos os rostos na imagem
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        face_id = "Desconhecido"

        if True in matches:
            first_match_index = matches.index(True)
            face_id = known_face_names[first_match_index]
        else:
            known_face_encodings.append(face_encoding)
            face_id = f"Pessoa {len(known_face_encodings)}"
            known_face_names.append(face_id)

        # Atualiza contador
        if face_id in face_counter:
            face_counter[face_id] += 1
        else:
            face_counter[face_id] = 1

        # Salva log
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        save_log(face_id, timestamp)
    
    # Exibir o vídeo (opcional)
    cv2.imshow('Video', frame)
    
    # Pressione 'q' para sair do loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
