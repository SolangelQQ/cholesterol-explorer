document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('sendButton').addEventListener('click', sendMessage);
});

function addMessage(message, sender) {
    const messageElement = document.createElement('div');
    messageElement.classList.add('message', sender);
    messageElement.textContent = message;
    document.getElementById('messages').appendChild(messageElement);
    document.getElementById('messages').scrollTop = document.getElementById('messages').scrollHeight;
}

function sendMessage() {
    const userInput = document.getElementById('userInput').value;
    if (userInput.trim() === '') return;
    addMessage(userInput, 'user');

    fetch('http://127.0.0.1:5000/chatbot', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ question: userInput })
    })
    .then(response => response.json())
    .then(data => {
        addMessage(data.response, 'bot');
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('response').textContent = 'Hubo un error al procesar tu pregunta.';
    });

    document.getElementById('userInput').value = '';
}
