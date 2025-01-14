from cryptography.fernet import Fernet
from flask import Flask, render_template

app = Flask(__name__)

# Génération de la clé de chiffrement et création de l'objet Fernet
key = Fernet.generate_key()
f = Fernet(key)

@app.route('/')
def hello_world():
    return "Bienvenue sur l'application de chiffrement et déchiffrement !"

@app.route('/exercice1')
def exo1():
     return render_template('exercice1.html')

@app.route('/exercice2')
def exo2():
     return render_template('exercice2.html')

@app.route('/exercice3')
def exo3():
     return render_template('exercice3.html')

@app.route('/exercice4')
def exo4():
     return render_template('exercice4.html')

@app.route('/coucou')
def exo5():
     return render_template('coucou.html')

@app.route('/maison')
def exo6():
     return render_template('maison.html')

@app.route('/jack')
def exo7():
     return render_template('jack.html')
    
@app.route('/encrypt/<string:valeur>')
def encryptage(valeur):
    valeur_bytes = valeur.encode()  # Conversion str -> bytes
    token = f.encrypt(valeur_bytes)  # Encrypt la valeur
    return f"Valeur encryptée : {token.decode()}"  # Retourne le token en str

# Exercice 1 : Route pour décryptage
@app.route('/decrypt/<string:token>')
def decryptage(token):
    try:
        token_bytes = token.encode()  # Conversion str -> bytes
        valeur_decryptee = f.decrypt(token_bytes)  # Décryptage du token
        return f"Valeur décryptée : {valeur_decryptee.decode()}"  # Retourne la valeur décryptée en str
    except Exception as e:
        return f"Erreur lors du décryptage : {e}"

if __name__ == "__main__":
    app.run(debug=True)
