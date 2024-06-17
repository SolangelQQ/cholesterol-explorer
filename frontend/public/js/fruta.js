navigator.mediaDevices.getUserMedia({ video: true })
    .then(function(stream) {
        var video = document.getElementById('video');
        video.srcObject = stream;
    })
    .catch(function(err) {
        console.log("Error al acceder a la cámara: " + err);
    });

document.getElementById('captureButton').addEventListener('click', function() {
    var canvas = document.getElementById('canvas');
    var context = canvas.getContext('2d');
    var video = document.getElementById('video');
    
    context.drawImage(video, 0, 0, canvas.width, canvas.height);
    
    var imageData = canvas.toDataURL('image/jpeg');
    
    fetch('/identify-fruit', {
        method: 'POST',
        body: JSON.stringify({ image: imageData }),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Error en la solicitud: ' + response.status);
        }
        return response.json();
    })
    .then(data => {
        var resultDiv = document.getElementById('result');
        resultDiv.innerHTML = "<h3>" + data.fruit + "</h3>";
        resultDiv.innerHTML += "<p>Beneficios:</p>";
        resultDiv.innerHTML += "<ul>";
        data.benefits.forEach(function(benefit) {
            resultDiv.innerHTML += "<li>" + benefit + "</li>";
        });
        resultDiv.innerHTML += "</ul>";
    })
    .catch(error => console.error('Error:', error));
});
