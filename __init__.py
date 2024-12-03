from cryptography.fernet import Fernet
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('hello.html')  # Page de test simple

# Génération d'une clé de cryptage unique
key = Fernet.generate_key()
f = Fernet(key)

@app.route('/encrypt/<string:valeur>')
def encryptage(valeur):
    valeur_bytes = valeur.encode()  # Conversion str -> bytes
    token = f.encrypt(valeur_bytes)  # Encrypt la valeur
    return f"Valeur encryptée : {token.decode()}"  # Retourne le token en str

# Nouvelle route : Décryptage d'une valeur
@app.route('/decrypt/', methods=['POST'])
def decryptage():
    try:
        data = request.json  # Récupère le JSON envoyé
        if 'encrypted_message' not in data:
            return jsonify({'error': 'Encrypted message is required'}), 400
        
        encrypted_message = data['encrypted_message']
        decrypted_message = f.decrypt(encrypted_message.encode()).decode()  # Décryptage
        return jsonify({'decrypted': decrypted_message})  # Retourne la valeur décryptée
    except Exception as e:
        return jsonify({'error': 'Decryption failed', 'details': str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
