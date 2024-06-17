document.addEventListener('DOMContentLoaded', () => {
    const username = localStorage.getItem('username');
    const userProfile = JSON.parse(localStorage.getItem('userProfile'));

    if (!userProfile) {
        alert('No se encontró información del perfil. Por favor, inicie sesión nuevamente.');
        window.location.href = '../../index.html';
        return;
    }

    document.getElementById('settingsName').value = userProfile.name || '';
    document.getElementById('settingsAge').value = userProfile.age || '';
    document.getElementById('settingsGender').value = userProfile.gender || '';
    document.getElementById('settingsHeight').value = userProfile.height || '';
    document.getElementById('settingsWeight').value = userProfile.weight || '';
    document.getElementById('settingsHealthGoal').value = userProfile.healthGoal || '';
    document.getElementById('settingsDiet').value = userProfile.diet || '';
    document.getElementById('settingsAllergies').value = userProfile.allergies || '';

    document.getElementById('saveSettings').addEventListener('click', () => {
        const updatedProfile = {
            username: username,
            name: document.getElementById('settingsName').value,
            age: document.getElementById('settingsAge').value,
            gender: document.getElementById('settingsGender').value,
            height: document.getElementById('settingsHeight').value,
            weight: document.getElementById('settingsWeight').value,
            healthGoal: document.getElementById('settingsHealthGoal').value,
            diet: document.getElementById('settingsDiet').value,
            allergies: document.getElementById('settingsAllergies').value
        };

        fetch(`http://localhost:5000/update/${username}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(updatedProfile)
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Error al actualizar el perfil.');
            }
            return response.json();
        })
        .then(data => {
            if (data.success) {
                alert('Perfil actualizado con éxito.');
                localStorage.setItem('userProfile', JSON.stringify(updatedProfile));
                window.location.reload();
            } else {
                alert('Error al actualizar el perfil: ' + data.error);
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('Error al actualizar el perfil.');
        });
    });
});
