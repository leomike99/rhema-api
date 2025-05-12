from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if email and password:
        return jsonify({'message': 'Connexion réussie'}), 200
    return jsonify({'error': 'Email ou mot de passe manquant'}), 400

@app.route('/api/presence', methods=['POST'])
def presence():
    data = request.get_json()
    nom = data.get('nom')
    departement = data.get('departement')
    date = data.get('date')

    if nom and departement and date:
        return jsonify({'message': f'Présence enregistrée pour {nom}'}), 200
    return jsonify({'error': 'Informations manquantes'}), 400

if __name__ == '__main__':
    app.run()