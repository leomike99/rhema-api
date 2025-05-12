from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return '✅ API Flask Rhema est active.'

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    if email == 'admin@eglise.com' and password == 'admin123':
        return jsonify({'success': True, 'message': 'Connexion réussie ✅'})
    else:
        return jsonify({'success': False, 'message': 'Identifiants invalides ❌'})
