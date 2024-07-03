import cv2

# Carregar o classificador Haar Cascade para detecção de rostos
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Capturar vídeo da webcam
cap = cv2.VideoCapture(0)

# Inicializar a variável de estado
pessoa_identificada = False

while True:
    # Ler um frame da webcam
    ret, frame = cap.read()
    if not ret:
        break

    # Converter o frame para escala de cinza (necessário para a detecção)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectar rostos no frame
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Verificar se algum rosto foi detectado
    if len(faces) > 0:
        if not pessoa_identificada:
            print("Pessoa Identificada")
            pessoa_identificada = True
    else:
        if pessoa_identificada:
            print("Nenhuma pessoa identificada")
            pessoa_identificada = False

    # Mostrar o frame com as detecções (opcional)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cv2.imshow('Webcam', frame)

    # Pressionar 'q' para sair do loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar o objeto de captura e fechar as janelas
cap.release()
cv2.destroyAllWindows()
