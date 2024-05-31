
from flask import Flask, jsonify, request
from flask_cors import CORS
import google.generativeai as ggi

app = Flask(__name__)
CORS(app)

def initialize_chatbot():
    fetcheed_api_key = "AIzaSyAzFvpz7EfB1RJIN9zT_QwWPMu-pkPYrlI"
    ggi.configure(api_key=fetcheed_api_key)
    model = ggi.GenerativeModel("gemini-pro")
    chat = model.start_chat()
    return chat

chat = initialize_chatbot()

def LLM_Response(question):
    response = chat.send_message(question, stream=True)
    return response

@app.route('/chatbot', methods=['POST'])
def chatbot():
    data = request.get_json()
    if not data or 'question' not in data:
        return jsonify({'error': 'No se proporcionó una pregunta válida.'}), 400
    question = data['question']
    response = LLM_Response(question)
    response_text = ''.join([word.text.replace("*", "") for word in response])
    return jsonify({'response': response_text})

if __name__ == '__main__':
    app.run(debug=True)
