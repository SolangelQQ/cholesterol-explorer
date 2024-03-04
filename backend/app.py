from flask import Flask, jsonify
from flask_cors import CORS  # Importa la extensión

app = Flask(__name__)
CORS(app)  # Habilita CORS para toda la aplicación

@app.route('/')
def hello_world():
    return jsonify(message="¡Hola desde el backend en Python!")

if __name__ == '__main__':
    app.run(debug=True)