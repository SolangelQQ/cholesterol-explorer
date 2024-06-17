document.getElementById('selectImageButton').addEventListener('change', function(event) {
    var file = event.target.files[0];
    var reader = new FileReader();

    var fileNameElement = document.getElementById('fileName');
    if (file) {
        fileNameElement.textContent = file.name;
    } else {
        fileNameElement.textContent = 'Ningún archivo seleccionado';
    }
    
    reader.onload = function(e) {
        var imageData = e.target.result;
        
        var imgElement = document.getElementById('selectedImage');
        imgElement.src = imageData;
        imgElement.style.display = 'block';

        var canvas = document.getElementById('canvas');
        var context = canvas.getContext('2d');
        var img = new Image();
        
        img.onload = function() {
            context.drawImage(img, 0, 0, canvas.width, canvas.height);
            
            sendImageToBackend(canvas.toDataURL('image/jpeg'));
        };
        
        img.src = imageData;
    };
    
    reader.readAsDataURL(file);
});

function sendImageToBackend(imageData) {
    fetch('http://localhost:5000/identify-fruit', {
        method: 'POST',
        body: JSON.stringify({ image: imageData }),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
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
}
