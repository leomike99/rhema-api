from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Rhema API déployée avec succès !"

@app.route('/api/login', methods=['POST'])
def api_login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    # Test simplifié : accepte n'importe quel email/mot de passe
    if email and password:
        return jsonify({"message": "Connexion réussie"}), 200
    return jsonify({"message": "Email ou mot de passe manquant"}), 400

if __name__ == "__main__":
    app.run()
