from flask import Flask
from backend.routes.health_routes import health_bp

app = Flask(__name__)
app.register_blueprint(health_bp)

if __name__ == '__main__':
    app.run(debug=True)
