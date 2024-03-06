document.addEventListener('DOMContentLoaded', () => {
    const calculatorForm = document.getElementById('calculatorForm');

    calculatorForm.addEventListener('submit', (event) => {
        event.preventDefault();

        const num1 = parseFloat(document.getElementById('num1').value);
        const num2 = parseFloat(document.getElementById('num2').value);

        console.log("num1:", num1);
        console.log("num2:", num2);

        sumar(num1, num2);
    });
});

function sumar(num1, num2) {
    fetch('http://localhost:5000/sumar', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ num1, num2 }),
        mode: 'cors',
        credentials: 'same-origin',
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerText = `Resultado: ${data.resultado}`;
    })
    .catch(error => console.error('Error al conectar con el backend:', error));
}
