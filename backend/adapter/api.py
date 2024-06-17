from flask import request, jsonify
from core.services import UserService, CholesterolService, ChatService, FruitService
from io import BytesIO
import base64
from PIL import Image
import json

def init_api(app):
    @app.route('/')
    def hello_world():
        return jsonify(message="¡Hola desde el backend en Python!")

    @app.route('/update/<username>', methods=['PUT'])
    def update_user(username):
        return UserService.update_user(username, request.json)

    @app.route('/calculate-cholesterol', methods=['POST'])
    def calcular_colesterol():
        return CholesterolService.calculate_cholesterol(request.get_json())

    @app.route('/chatbot', methods=['POST'])
    def chatbot():
        data = request.get_json()
        if not data or 'question' not in data:
            return jsonify({'error': 'No se proporcionó una pregunta válida.'}), 400
        question = data['question']
        response = ChatService.get_response(question)
        return jsonify({'response': response})

    @app.route('/login', methods=['POST'])
    def login():
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        return UserService.login(username, password)
    
    @app.route('/users')
    def get_users():
        with open('users.json', 'r', encoding='utf-8') as file:
            users_data = json.load(file)
        return jsonify(users=users_data['users'])

    @app.route('/identify-fruit', methods=['POST'])
    def identify_fruit():
        data = request.get_json()
        image_data = data.get('image')

        if not image_data:
            return jsonify({"error": "No image data provided"}), 400

        try:
            image_data = image_data.split(",")[1]
            image = Image.open(BytesIO(base64.b64decode(image_data)))
        except Exception as e:
            return jsonify({"error": "Invalid image file"}), 400

        fruit_name, fruit_benefits = FruitService.identify_fruit(image)
        
        return jsonify({
            "fruit": fruit_name,
            "benefits": fruit_benefits
        })
