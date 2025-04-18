from flask import Flask
from flask import session

def create_app():
    app = Flask(__name__)
    app.secret_key = 'your_super_secret_key'  # ✅ Required for session to work

    # Import blueprints
    from app.routes.home import home_bp
    from app.routes.civil import civil_bp
    from app.routes.mechanical import mechanical_bp
    from app.routes.electrical import electrical_bp
    from app.routes.history import history_bp  # ✅ Add this line

    # Register blueprints
    app.register_blueprint(home_bp)
    app.register_blueprint(civil_bp, url_prefix='/civil')
    app.register_blueprint(mechanical_bp, url_prefix='/mechanical')
    app.register_blueprint(electrical_bp, url_prefix='/electrical')
    app.register_blueprint(history_bp)  # ✅ Add this line

    return app
