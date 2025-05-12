from flask import Blueprint, request, jsonify
from datetime import datetime
from utils.db import get_db

presence_bp = Blueprint('presence', __name__)

@presence_bp.route('/api/presence/scan', methods=['POST'])
def scan_presence():
    data = request.get_json()
    user_id = data.get("user_id")  # ou "code" si tu veux un code unique
    if not user_id:
        return jsonify({"error": "Missing user_id"}), 400

    db = get_db()
    db.execute(
        "INSERT INTO presence (user_id, timestamp) VALUES (?, ?)",
        (user_id, datetime.now())
    )
    db.commit()

    return jsonify({"message": "Présence enregistrée"}), 200
