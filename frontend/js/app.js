document.addEventListener('DOMContentLoaded', () => {
    const calculatorForm = document.getElementById('calculatorForm');

    calculatorForm.addEventListener('submit', (event) => {
        event.preventDefault();

        const tf = parseFloat(document.getElementById('tf').value);
        const presente = parseFloat(document.getElementById('presente').value);

        predecir_colesterol(tf, presente);
    });
});

function predecir_colesterol(tf, presente) {
    fetch('http://localhost:5000/calculate-cholesterol', {
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
        drawChart(data.resultado.tiempos, data.resultado.futuros);
    })
    .catch(error => console.error('Error al conectar con el backend:', error));
}

function drawChart(tiempos, futuros) {
    const ctx = document.getElementById('myChart').getContext('2d');

    const myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: tiempos,
            datasets: [{
                label: 'Futuros',
                data: futuros,
                borderColor: 'rgb(75, 192, 192)',
                borderWidth: 2,
                fill: false,
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                x: {
                    type: 'linear',
                    position: 'bottom'
                },
                y: {
                    type: 'linear',
                    position: 'left'
                }
            }
        }
    });
}


