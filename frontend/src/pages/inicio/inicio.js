document.addEventListener('DOMContentLoaded', (event) => {
    const ctx = document.getElementById('healthChart').getContext('2d');
    const healthChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio'],
            datasets: [{
                label: 'Colesterol LDL (mg/dL)',
                data: [130, 125, 120, 115, 110, 105],
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 2,
                fill: false
            }, {
                label: 'Peso (kg)',
                data: [80, 78, 76, 74, 72, 70],
                borderColor: 'rgba(153, 102, 255, 1)',
                borderWidth: 2,
                fill: false
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: false
                }
            }
        }
    });
});
