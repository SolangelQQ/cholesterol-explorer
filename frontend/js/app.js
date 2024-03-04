document.addEventListener('DOMContentLoaded', () => {
    fetch('http://localhost:5000/', { mode: 'cors' })
        .then(response => {
            if (!response.ok) {
                throw new Error(`Network response was not ok: ${response.status} ${response.statusText}`);
            }
            return response.json();  // Cambiado a json para manejar la respuesta como un objeto JSON
        })
        .then(data => {
            // Asegúrate de que `data.message` contiene el mensaje que deseas mostrar
            document.getElementById('message').innerText = data.message;
        })
        .catch(error => console.error('Error al conectar con el backend:', error));
});
