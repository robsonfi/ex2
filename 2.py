from flask import Flask, request, jsonify
import speech_recognition as sr

app = Flask(__name__)

@app.route('/transcrever', methods=['POST'])
def transcrever_audio():
    arquivo = request.files['file']
    reconhecedor = sr.Recognizer()

    with sr.AudioFile(arquivo) as source:
        audio = reconhecedor.record(source)
        texto = reconhecedor.recognize_google(audio, language='pt-BR')
    
    return jsonify({"transcricao": texto})

if __name__ == '__main__':
    app.run(debug=True)
