from cryptography.fernet import Fernet
from flask import Flask, jsonify, request

app = Flask(__name__)

# Génération d'une clé unique pour l'application
key = Fernet.generate_key()
f = Fernet(key)

@app.route('/')
def hello_world():
    return "Bienvenue sur l'API de cryptage/décryptage !"  # Message d'accueil

# Route pour crypter une valeur
@app.route('/encrypt/<string:valeur>')
def encryptage(valeur):
    token = f.encrypt(valeur.encode())  # Cryptage de la valeur
    return f"Valeur encryptée : {token.decode()}"  # Retour du texte crypté

# Route pour décrypter une valeur
@app.route('/decrypt/', methods=['POST'])
def decryptage():
    data = request.json
    if 'encrypted_message' not in data:
        return jsonify({'error': 'Encrypted message is required'}), 400

    try:
        decrypted_message = f.decrypt(data['encrypted_message'].encode()).decode()  # Décryptage
        return jsonify({'decrypted': decrypted_message})  # Retour du texte décrypté
    except Exception as e:
        return jsonify({'error': 'Invalid encrypted message', 'details': str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
