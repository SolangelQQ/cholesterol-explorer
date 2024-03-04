document.addEventListener('DOMContentLoaded', () => {
    fetch('http://localhost:5000/', { mode: 'cors' })
        .then(response => {
            if (!response.ok) {
                throw new Error(`Network response was not ok: ${response.status} ${response.statusText}`);
            }
            return response.json();
        })
        .then(data => {
            document.getElementById('message').innerText = data.message;
        })
        .catch(error => console.error('Error al conectar con el backend:', error));
});
