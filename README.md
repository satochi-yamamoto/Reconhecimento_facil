Aplicação de Detecção de Rostos com Webcam
Este projeto é uma aplicação simples em Python para detectar rostos usando a webcam do computador. Ele utiliza a biblioteca OpenCV para capturar o vídeo da webcam e a biblioteca dlib com o modelo Haar Cascade para detectar rostos em tempo real.

Funcionalidades
Detecta rostos em tempo real usando a webcam do computador.
Exibe uma mensagem quando um rosto é detectado.
Conta e exibe o número de rostos detectados em intervalos de tempo configuráveis.
Permite selecionar o dispositivo de câmera ativa no computador.
Requisitos de Instalação
Para executar esta aplicação, você precisa ter instalado:

Python (versão 3.6 ou superior)
OpenCV (pip install opencv-python)
dlib (pip install dlib) - Requer o CMake instalado no sistema.
face-recognition (pip install face-recognition)
Certifique-se de que o CMake esteja instalado antes de instalar o dlib. Se você encontrar problemas durante a instalação do dlib, consulte as instruções de instalação específicas para o seu sistema operacional.

Como Usar
Clone o repositório:

bash
Copiar código
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio
Instale as dependências:

bash
Copiar código
pip install -r requirements.txt
Certifique-se de que todas as dependências listadas no requirements.txt estão instaladas corretamente.

Execute a aplicação:

bash
Copiar código
python main.py
Isso iniciará a aplicação de detecção de rostos usando a webcam.
Pressione q para sair da aplicação.
Personalize as configurações (opcional):

Você pode modificar os parâmetros no código-fonte para ajustar a tolerância de detecção de rostos, intervalos de contagem, etc.
Contribuições
Contribuições são bem-vindas! Se você quiser melhorar esta aplicação, sinta-se à vontade para enviar pull requests.

Licença
Este projeto está licenciado sob a MIT License.
