import cv2
import face_recognition
import datetime

# Inicializa a captura de vídeo da webcam (padrão: dispositivo 0)
cap = cv2.VideoCapture(0)

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

    # Exibir o vídeo com os rostos identificados
    for (top, right, bottom, left), face_id in zip(face_locations, known_face_names):
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.putText(frame, face_id, (left + 6, bottom - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

    cv2.imshow('Video', frame)

    # Pressione 'q' para sair do loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
