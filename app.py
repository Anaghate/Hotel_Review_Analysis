from flask import Flask
from config import Config
from routes.user_routes import user_bp
from routes.owner_routes import owner_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(user_bp)
    app.register_blueprint(owner_bp)

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)