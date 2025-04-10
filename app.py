from flask import Flask, request, jsonify
import os
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return open('index.html').read()  # Serwuje stronę HTML

@app.route('/generate', methods=['POST'])
def generate_link():
    data = request.get_json()  # Odbieramy dane w formacie JSON
    url = data.get('url')  # Pobieramy URL z JSONa

    if not url:
        return jsonify({'error': 'No URL provided'}), 400  # Zwracamy błąd, jeśli URL nie jest podany

    # Symulacja generowania linku - tutaj wstaw prawdziwy kod do integracji z Linkvertise
    link = f"https://linkvertise.com/{url}"  # Zastąp to prawdziwym mechanizmem API Linkvertise

    return jsonify({'link': link})  # Zwracamy link jako odpowiedź w formacie JSON

if __name__ == '__main__':
    # Pobierz port z zmiennej środowiskowej, jeśli jest dostępny, w przeciwnym razie ustaw port 5000
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
