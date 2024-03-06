from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return jsonify(message="¡Hola desde el backend en Python!")

@app.route('/sumar', methods=['POST'])
def sumar():
    try:
        data = request.get_json()
        num1 = float(data.get('num1', 0))  # Si 'num1' no está presente, establecerlo a 0
        num2 = float(data.get('num2', 0))  # Si 'num2' no está presente, establecerlo a 0
        resultado = num1 + num2
        return jsonify(resultado=resultado)
    except ValueError:
        return jsonify(error="Los datos proporcionados no son números válidos"), 400

        

if __name__ == '__main__':
    app.run(debug=True)
