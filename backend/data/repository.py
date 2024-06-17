import json
import google.generativeai as ggi
import base64
from io import BytesIO
from PIL import Image
import numpy as np
import os
import tensorflow as tf

class UserRepository:
    @staticmethod
    def load_users():
        with open('data/datasets/users.json', 'r') as file:
            return json.load(file)

    @staticmethod
    def save_users(users_data):
        with open('data/datasets/users.json', 'w') as file:
            json.dump(users_data, file, indent=4)

    @staticmethod
    def verify_credentials(users, username, password):
        for user in users:
            if user['username'] == username and user['password'] == password:
                return True
        return False

class ModelRepository:
    model_path = 'data/models/model.h5'

    if not os.path.exists(model_path):
        raise FileNotFoundError(f"The model file was not found at {model_path}. Please ensure the file is present.")

    model = tf.keras.models.load_model(model_path)

    fruit_labels = ['Manzana','Aguacate','Plátano','Cereza','Coco','Kiwi','Limón','Mango','Naranja']

    @staticmethod
    def preprocess_image(image):
        image = image.resize((100, 100)) 
        image = np.array(image) / 255.0
        image = np.expand_dims(image, axis=0)
        return image

    @staticmethod
    def identify_fruit(image):
        processed_image = ModelRepository.preprocess_image(image)
        predictions = ModelRepository.model.predict(processed_image)
        predicted_label_index = np.argmax(predictions)
        
        if predicted_label_index < len(ModelRepository.fruit_labels):
            fruit_name = ModelRepository.fruit_labels[predicted_label_index]
        else:
            fruit_name = "Unknown"
        
        fruit_benefits_dict = {
            "Manzana": ["Rica en fibra", "Fuente de vitamina C", "Buena para la digestión", "Ayuda a controlar el azúcar en la sangre"],
            "Aguacate": ["Rico en grasas saludables", "Fuente de vitamina E y potasio", "Bueno para el corazón", "Ayuda a absorber nutrientes de otros alimentos"],
            "Plátano": ["Alto en potasio", "Energía rápida", "Bueno para la presión arterial", "Ayuda a la digestión"],
            "Cereza": ["Antioxidantes", "Bajo en calorías", "Ayuda a reducir la inflamación", "Bueno para la salud del corazón"],
            "Coco": ["Alto en fibra", "Fuente de minerales como el manganeso", "Hidrata y mejora la piel", "Ayuda a la digestión"],
            "Kiwi": ["Alto en vitamina C", "Refuerza el sistema inmunológico", "Mejora la salud digestiva", "Rico en antioxidantes"],
            "Limón": ["Alto en vitamina C", "Refuerza el sistema inmunológico", "Ayuda a la digestión", "Bueno para la piel"],
            "Mango": ["Alto en vitamina C", "Refuerza el sistema inmunológico", "Bueno para la vista", "Rico en fibra"],
            "Naranja": ["Alto en vitamina C", "Refuerza el sistema inmunológico", "Bueno para la piel", "Ayuda a absorber el hierro de otros alimentos"],
            "No identificado": ["Beneficio desconocido"]
        }

        fruit_benefits = fruit_benefits_dict.get(fruit_name, ["Unknown benefit"])
        return fruit_name, fruit_benefits

    @staticmethod
    def decode_image(image_data):
        image_data = image_data.split(",")[1]
        image = Image.open(BytesIO(base64.b64decode(image_data)))
        return image

class ChatRepository:
    @staticmethod
    def initialize_chatbot():
        api_key = "AIzaSyAzFvpz7EfB1RJIN9zT_QwWPMu-pkPYrlI"
        ggi.configure(api_key=api_key)
        model = ggi.GenerativeModel("gemini-pro")
        chat = model.start_chat()
        return chat
