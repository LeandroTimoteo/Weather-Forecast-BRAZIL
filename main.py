import os
import sys
from flask import Flask, send_from_directory
from src.models.user import db
from src.routes.user import user_bp
from src.routes.weather import weather_bp

# Garantir que src está no path
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

app = Flask(__name__, static_folder=os.path.join(os.path.dirname(__file__), 'static'))
app.config['SECRET_KEY'] = 'asdf#FGSgvasgf$5$WGT'

# Blueprints
app.register_blueprint(user_bp, url_prefix='/api')
app.register_blueprint(weather_bp, url_prefix='/api')

# Configuração do banco
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(os.path.dirname(__file__), 'database', 'app.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
with app.app_context():
    db.create_all()

# Rotas estáticas
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    static_folder_path = app.static_folder
    if static_folder_path is None:
        return "Static folder not configured", 404

    if path != "" and os.path.exists(os.path.join(static_folder_path, path)):
        return send_from_directory(static_folder_path, path)
    else:
        index_path = os.path.join(static_folder_path, 'index.html')
        if os.path.exists(index_path):
            return send_from_directory(static_folder_path, 'index.html')
        else:
            
            return "index.html not found", 404

# Importante: NÃO abrir navegador no Render
if __name__ == '__main__':
    # Apenas para rodar localmente
    app.run(host='0.0.0.0', port=5000, debug=True)
