from flask import Blueprint, jsonify

health_bp = Blueprint('health', __name__)

@health_bp.route('/', methods=['GET'])
def home():
    return jsonify({
        "message": "Task application is running",
        "health": "/health"
    })

@health_bp.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"})
