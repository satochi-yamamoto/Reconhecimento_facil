import cv2
import time

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

# Carregar o classificador Haar Cascade para detecção de rostos
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Capturar vídeo da câmera selecionada
cap = cv2.VideoCapture(available_cameras[camera_index])

# Inicializar variáveis
pessoa_identificada = False
face_count = 0
start_time = time.time()
count_interval = 10  # Intervalo de tempo em segundos para exibir a contagem

# Definir a área mínima para considerar um rosto como legível
min_face_area = 5000

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

    # Converter o frame para escala de cinza (necessário para a detecção)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectar rostos no frame
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Verificar se algum rosto legível foi detectado
    face_detected = False
    for (x, y, w, h) in faces:
        if w * h >= min_face_area:  # Verificar se a área do rosto é maior que a área mínima
            face_detected = True
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)  # Desenhar um retângulo em torno do rosto

    if face_detected:
        if not pessoa_identificada:
            print("Pessoa Identificada")
            pessoa_identificada = True
            face_count += 1  # Incrementar a contagem de rostos identificados
    else:
        if pessoa_identificada:
            print("Nenhuma pessoa identificada")
            pessoa_identificada = False

    # Mostrar o frame com as detecções
    cv2.imshow('Webcam', frame)

    # Verificar se o intervalo de tempo passou e exibir a contagem
    current_time = time.time()
    if current_time - start_time >= count_interval:
        print(f"Rostos identificados nos últimos {count_interval} segundos: {face_count}")
        face_count = 0  # Resetar a contagem
        start_time = current_time  # Resetar o tempo de início

    # Pressionar 'q' para sair do loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar o objeto de captura e fechar as janelas
cap.release()
cv2.destroyAllWindows()
0
