document.addEventListener('DOMContentLoaded', () => {
    const calculatorForm = document.getElementById('calculatorForm');

    calculatorForm.addEventListener('submit', (event) => {
        event.preventDefault();

        const tf = parseFloat(document.getElementById('tf').value);
        const presente = parseFloat(document.getElementById('presente').value);

        sumar(tf, presente);
    });
});

function sumar(tf, presente) {
    fetch('http://localhost:5000/sumar', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ tf, presente }),
        mode: 'cors',
        credentials: 'same-origin',
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerText = `Tiempos: ${data.resultado.tiempos.join(', ')}\nFuturos: ${data.resultado.futuros.join(', ')}`;
    })
    .catch(error => console.error('Error al conectar con el backend:', error));
}
