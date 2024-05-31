document.addEventListener('DOMContentLoaded', (event) => {
    const video = document.getElementById('video');

    // Solicita acceso a la cámara del usuario
    navigator.mediaDevices.getUserMedia({ video: true })
        .then((stream) => {
            // Asigna el stream de video al elemento video
            video.srcObject = stream;
        })
        .catch((err) => {
            console.error('Error al acceder a la cámara: ', err);
            alert('No se pudo acceder a la cámara.');
        });
});
