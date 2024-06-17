document.addEventListener('DOMContentLoaded', (event) => {
    const userProfile = JSON.parse(localStorage.getItem('userProfile'));
    if (!userProfile) {
        alert('No se encontró información del perfil. Por favor, inicie sesión nuevamente.');
        window.location.href = '../../index.html';
        return;
    }

    const ctx = document.getElementById('healthChart').getContext('2d');
    const healthChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: userProfile.healthData.cholesterol.labels,
            datasets: [{
                label: 'Colesterol LDL (mg/dL)',
                data: userProfile.healthData.cholesterol.values,
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 2,
                fill: false
            }, {
                label: 'Peso (kg)',
                data: userProfile.healthData.weight.values,
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

    const goalsList = document.getElementById('goalsList');
    userProfile.goals.forEach(goal => {
        const li = document.createElement('li');
        li.textContent = `${goal.exercise}: ${goal.amount}`;
        goalsList.appendChild(li);
    });

    document.getElementById('profileName').textContent = userProfile.name;
    document.getElementById('profileHealthGoal').textContent = userProfile.healthGoal;
    document.getElementById('profileAge').textContent = userProfile.age;
    document.getElementById('profileGender').textContent = userProfile.gender;
    document.getElementById('profileAllergies').textContent = userProfile.allergies;
    document.getElementById('profileHeight').textContent = userProfile.height;
    document.getElementById('profileWeight').textContent = userProfile.weight;
    document.getElementById('profileDiet').textContent = userProfile.diet;

    document.getElementById('logout').addEventListener('click', () => {
        localStorage.removeItem('userProfile');
        window.location.href = '../../index.html';
    });
});

function showCredentials() {
    fetch('http://localhost:5000/users') // Reemplaza con tu ruta correcta
        .then(response => response.json())
        .then(data => {
            const userList = document.getElementById('userList');
            userList.innerHTML = ''; // Limpiar lista anterior

            data.users.forEach(user => {
                const listItem = document.createElement('li');
                listItem.innerHTML = `
                    <div class="username">${user.username}</div>
                    <div class="password">Contraseña: ${user.password}</div>
                `;
                userList.appendChild(listItem);
            });
        })
        .catch(error => console.error('Error al obtener usuarios:', error));
}