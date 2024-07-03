import cv2
import face_recognition
import time
import numpy as np

def is_image_blurry(image, threshold=100):
    # Calcular a variação de Laplace da imagem para verificar a clareza
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    laplacian_var = cv2.Laplacian(gray, cv2.CV_64F).var()
    return laplacian_var < threshold

def list_cameras():
    # Tentar acessar os dispositivos de câmera para listar disponíveis
    index = 0
    arr = []
    while True:
        cap = cv2.VideoCapture(index)
        if not cap.read()[0]:
            break
        else:
            arr.append(index)
        cap.release()
        index += 1
    return arr

# Listar dispositivos de câmera disponíveis
available_cameras = list_cameras()
print("Dispositivos de câmera disponíveis:")
for idx, cam in enumerate(available_cameras):
    print(f"{idx}: Câmera {cam}")

# Solicitar ao usuário para escolher um dispositivo de câmera
camera_index = int(input("Selecione o índice do dispositivo de câmera que deseja usar: "))

# Capturar vídeo da câmera selecionada
cap = cv2.VideoCapture(available_cameras[camera_index])

# Inicializar variáveis
pessoa_identificada = False
face_count = 0
known_faces_encodings = []
start_time = time.time()
count_interval = 10  # Intervalo de tempo em segundos para exibir a contagem

while True:
    # Ler um frame da câmera
    ret, frame = cap.read()
    if not ret:
        break

    # Verificar se a imagem está borrada
    if is_image_blurry(frame):
        if pessoa_identificada:
            print("Nenhuma pessoa identificada (imagem borrada)")
            pessoa_identificada = False
        continue

    # Converter o frame para RGB (necessário para a face_recognition)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detectar rostos no frame
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    # Verificar se algum rosto legível foi detectado
    face_detected = False
    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_faces_encodings, face_encoding, tolerance=0.6)
        if not any(matches):  # Se não houver correspondência com rostos conhecidos
            known_faces_encodings.append(face_encoding)  # Adicionar novo rosto conhecido
            face_count += 1  # Incrementar a contagem de rostos identificados
            face_detected = True

    if face_detected:
        if not pessoa_identificada:
            print("Pessoa Identificada")
            pessoa_identificada = True
    else:
        if pessoa_identificada:
            print("Nenhuma pessoa identificada")
            pessoa_identificada = False

    # Mostrar o frame com as detecções
    for (top, right, bottom, left) in face_locations:
        cv2.rectangle(frame, (left, top), (right, bottom), (255, 0, 0), 2)  # Desenhar um retângulo em torno do rosto

    cv2.imshow('Webcam', frame)

    # Verificar se o intervalo de tempo passou e exibir a contagem
    current_time = time.time()
    if current_time - start_time >= count_interval:
        print(f"Rostos identificados no total: {face_count}")
        start_time = current_time  # Resetar o tempo de início

    # Pressionar 'q' para sair do loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar o objeto de captura e fechar as janelas
cap.release()
cv2.destroyAllWindows()
