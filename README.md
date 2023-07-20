# CLIV - Assistente Virtual 🗣️
<img src="https://www.ambientelivre.com.br/images/logos_open_source/tensorflow_logo.png" alt="Minha Imagem" width="500" height="auto" />


CLIV é uma Assistente Virtual baseada em inteligência artificial, desenvolvida para interagir por meio de comandos de voz e realizar tarefas diversas, como fornecer informações sobre data e hora, abrir programas no sistema operacional e muito mais.

## Funcionalidades 🎛️

- Reconhecimento de comandos de voz utilizando a biblioteca Vosk.
- Síntese de fala para interação com o usuário, empregando a biblioteca pyttsx3.
- Utilização do TensorFlow e Keras para reconhecimento de fala.

## Instalação 💻

1. Clone o repositório do projeto para o seu ambiente local:
```bash
git clone https://github.com/theastro1/VoiceAssistant-CLIV.git
cd VoiceAssistant-CLIV
```
2. Recomenda-se a criação de um ambiente virtual para isolar as dependências do projeto:
```bash
python3 -m venv venv
```
3. Ative o ambiente virtual:
- Windows:
```bash
venv\Scripts\activate
```
- Linux/Mac:
```bash
source venv/bin/activate
```
4. Instale as dependências do projeto a partir do arquivo `requirements.txt`:
```bash
pip install -r requirements.txt
```
5. Execute a CLIV com:
```bash
python cliv.py
```
Agora você pode interagir com a CLIV através de comandos de voz!

## Como Utilizar ❓

Assim que executar o código, a CLIV irá exigir um código secreto para se apresentar. Digite o código correto e ela irá se apresentar. Após a apresentação, você pode dar comandos de voz para realizar ações específicas. Algumas funcionalidades disponíveis são:

- Pergunte a CLIV sobre a data e hora atual.
- Peça para ela abrir o bloco de notas ou o Google Chrome.
- Defina um nome personalizado para a assistente virtual.
- Encerre a interação com a assistente.

## Sobre as Tecnologias 🛠️

A CLIV utiliza a biblioteca Vosk para reconhecimento de fala e interpretação dos comandos do usuário. Para a síntese de fala, a biblioteca pyttsx3 é utilizada para interagir com o usuário. Além disso, a CLIV também utiliza TensorFlow e Keras para realizar o reconhecimento de fala e processar os dados recebidos.

## Contribuição 👥

Contribuições são bem-vindas! Caso queira contribuir com o projeto, sinta-se à vontade para abrir uma "issue" relatando problemas ou criar um "pull request" com melhorias e novas funcionalidades.

## Licença 📜

Este projeto é licenciado sob a [Licença MIT](https://opensource.org/licenses/MIT). Sinta-se à vontade para usá-lo e modificá-lo de acordo com as suas necessidades.

---
