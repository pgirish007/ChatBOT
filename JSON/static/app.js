window.onload = function() {
    fetch('/get_user')
    .then(response => response.json())
    .then(data => {
        const userForm = document.getElementById('userForm');
        for (const key in data) {
            if (data.hasOwnProperty(key)) {
                const input = document.createElement('input');
                input.setAttribute('type', 'text');
                input.setAttribute('id', key);
                input.setAttribute('value', data[key]);
                input.setAttribute('placeholder', `Enter ${key}`);
                userForm.appendChild(input);
            }
        }
    })
    .catch(error => console.error('Error:', error));
};

function updateUserData() {
    const userData = {};
    const inputs = document.querySelectorAll('#userForm input');
    inputs.forEach(input => {
        userData[input.id] = input.value;
    });

    fetch('/update_user', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(userData)
    })
    .then(response => response.json())
    .then(data => {
        const userList = document.getElementById('userList');
        userList.innerHTML = `
            <p>ID: ${data.id}</p>
            <p>Name: ${data.name}</p>
            <p>Age: ${data.age}</p>
        `;
    })
    .catch(error => console.error('Error:', error));
}
