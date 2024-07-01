# Webcam Face Detection

Este projeto é uma aplicação simples em Python que utiliza a webcam do computador para detectar rostos e contar quantas pessoas foram identificadas na frente da câmera. Ele usa a biblioteca `OpenCV` para captura de vídeo e detecção de rostos, e `face_recognition` para o reconhecimento e contagem de rostos.

## Pré-requisitos

Antes de começar, certifique-se de ter instalado o Python (versão 3.6 ou superior) e o pip (gerenciador de pacotes do Python) no seu sistema. Além disso, é necessário ter o CMake instalado para compilar o pacote `dlib`, que é uma dependência do `face_recognition`.

- Python 3.6 ou superior: [Python Downloads](https://www.python.org/downloads/)
- pip (instalado automaticamente com o Python)

## Instalação de Dependências

1. **Instalação do CMake**:
   - O `dlib` requer o CMake para compilar. Certifique-se de ter o CMake instalado no seu sistema. Você pode baixá-lo em [cmake.org](https://cmake.org/download/).

2. **Instalação das bibliotecas Python**:
   - Abra um terminal (ou prompt de comando) e execute o seguinte comando para instalar as bibliotecas necessárias:

     ```bash
     pip install opencv-python-headless face-recognition
     ```

## Como Usar

1. **Clone o Repositório**:
   - Clone este repositório para o seu computador:

     ```bash
     git clone https://github.com/ydsoftware1979/Reconhecimento_facil.git
     ```

2. **Execute o Script**:
   - Navegue até o diretório do projeto e execute o script Python:

     ```bash
     cd Reconhecimento_facil
     python webcam_face_detection.py
     ```

3. **Funcionamento**:
   - O script abrirá uma janela mostrando o feed de vídeo da webcam.
   - Ele detectará rostos na câmera e exibirá uma mensagem "Pessoa Identificada" sempre que um novo rosto for detectado.
   - A contagem de pessoas identificadas será exibida periodicamente no terminal.

4. **Finalização**:
   - Para sair do script, pressione `q` na janela do vídeo ou no terminal onde o script está sendo executado.

## Créditos

- **OpenCV**: Biblioteca de visão computacional utilizada para captura de vídeo e detecção de rostos.
- **face_recognition**: Biblioteca que fornece métodos simples para carregar, manipular e reconhecer faces usando Python e a biblioteca `dlib`.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir um issue ou enviar um pull request com melhorias.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
