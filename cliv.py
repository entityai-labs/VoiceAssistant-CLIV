#!/usr/bin/env python3

from vosk import Model, KaldiRecognizer
import os
import pyaudio
import pyttsx3
import json
import core
from nlu.classifier import classify

# Variável para armazenar o nome da assistente virtual
assistant_name = "CLIV"
# Código secreto para se apresentar
correct_code = "SEUCÓDIGO"  # Coloque o código correto aqui

# Síntese de fala
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[-2].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def get_user_code():
    while True:
        user_code = input("Digite o código secreto: ").strip().lower()
        if user_code == correct_code:
            return True
        else:
            print("Código incorreto. Tente novamente.")
            speak("Código incorreto. Tente novamente.")

def evaluate(text):
    global assistant_name

    # Reconhecer entidade do texto.
    entity = classify(text)
    if entity == 'time|getTime':
        speak(core.SystemInfo.get_time())
    elif entity == 'time|getDate':
        speak(core.SystemInfo.get_date())

    # Abrir programas
    elif entity == 'open|notepad':
        speak(f'Abrindo o bloco de notas, {assistant_name}. Se você precisar de algo mais, estou aqui para ajudar.')
        os.system('notepad.exe')
    elif entity == 'open|chrome':
        speak(f'Abrindo o Google Chrome, {assistant_name}. Se precisar de algo mais, é só me chamar.')
        os.system('"C:/Program Files/Google/Chrome/Application/chrome.exe"')

    print('Text: {}  Entity: {}'.format(text, entity))

# Reconhecimento de fala
model = Model('model')
rec = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=2048)
stream.start_stream()

# Exigir o código secreto
if get_user_code():
    # Saudações iniciais após o código correto ser fornecido
    speak(f"Olá, eu sou {assistant_name}, sua assistente virtual. Como posso ajudar, Meu Lorde?")

    # Loop do reconhecimento de fala
    while True:
        data = stream.read(2048)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            result = rec.Result()
            result = json.loads(result)

            if result is not None:
                text = result['text']
                evaluate(text)
else:
    # Encerrar o programa se o código estiver incorreto
    speak("Código incorreto. Você não é o meu criador. Até logo. Fechando programação.")
