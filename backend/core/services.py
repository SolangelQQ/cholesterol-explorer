import json
import numpy as np
from core.models import euler, colesterol
from data.repository import UserRepository, ModelRepository, ChatRepository
import PyPDF2
import logging

class UserService:
    @staticmethod
    def update_user(username, data):
        try:
            if not data or 'profile' not in data:
                return {'error': 'Solicitud incorrecta. Se requiere un cuerpo JSON con un campo "profile"'}, 400
            
            users_data = UserRepository.load_users()

            updated_profile = data.get('profile')
            new_username = data.get('username')
            new_password = data.get('password')

            user_found = False
            for user in users_data['users']:
                if user['username'] == username:
                    user['username'] = new_username
                    user['password'] = new_password
                    user['profile'].update(updated_profile)
                    user_found = True
                    break
            
            if not user_found:
                return {'error': f'Usuario {username} no encontrado'}, 404

            UserRepository.save_users(users_data)
            return {'success': True, 'message': 'Perfil actualizado correctamente'}, 200

        except FileNotFoundError:
            return {'error': 'Archivo users.json no encontrado'}, 500
        except KeyError as e:
            return {'error': f'Datos incorrectos en la solicitud: {str(e)}'}, 400
        except Exception as e:
            return {'error': str(e)}, 500

    @staticmethod
    def login(username, password):
        users = UserRepository.load_users()['users']
        if UserRepository.verify_credentials(users, username, password):
            user_profile = next((user['profile'] for user in users if user['username'] == username), None)
            return {'success': True, 'profile': user_profile}
        else:
            return {'success': False}

class CholesterolService:
    @staticmethod
    def calculate_cholesterol(data):
        try:
            tf = float(data.get('tf', 0))
            presente = float(data.get('presente', 0))

            t0 = 0
            cn = 200
            k1 = 0.1
            k2 = 0.1
            E = 400
            dt = 0.01

            tiempos, futuros = euler(t0, tf, presente, colesterol, dt, cn, k1, k2, E)
            resultado = {'tiempos': tiempos.tolist(), 'futuros': futuros.tolist()}
            return {'resultado': resultado}
        except ValueError:
            return {'error': "Los datos proporcionados no son números válidos"}, 400

class ChatService:
    @staticmethod
    def extraer_texto_pdf(ruta_pdf):
        try:
            with open(ruta_pdf, 'rb') as archivo_pdf:
                lector_pdf = PyPDF2.PdfReader(archivo_pdf)
                texto = ""
                for pagina in lector_pdf.pages:
                    texto += pagina.extract_text()
            return texto
        except Exception as e:
            logging.error(f'Error al extraer texto del PDF: {e}')
            return ""

    @staticmethod
    def get_question(question, ruta_pdf):
        try:
            texto_extraido = ChatService.extraer_texto_pdf(ruta_pdf)
            mensaje_completo = f"{texto_extraido.strip()}\n en base a esta base de dato respondeme {question.strip()}?"
            return mensaje_completo
        except Exception as e:
            logging.error(f'Error al obtener la pregunta: {e}')
            return ""

    @staticmethod
    def get_response(question):
        try:
            complete_question = ChatService.get_question(question, 'data/datasets/Menú semanal para adelgazar y bajar colesterol pdf.pdf')
            chat = ChatRepository.initialize_chatbot()
            response = chat.send_message(complete_question, stream=True)
            if response:
                response_text = ''.join([word.text.replace("*", "") for word in response])
                return response_text
            else:
                logging.warning('La respuesta del chatbot está vacía.')
                return "No se recibió una respuesta válida del chatbot."
        except Exception as e:
            logging.error(f'Error al obtener la respuesta: {e}')
            return "Error: No se pudo obtener la respuesta"

class FruitService:
    @staticmethod
    def identify_fruit(image):
        fruit_name, fruit_benefits = ModelRepository.identify_fruit(image)
        return fruit_name, fruit_benefits
