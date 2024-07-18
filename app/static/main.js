async function getUser() {
    const userId = document.getElementById('userId').value;
    const response = await fetch(`/get-user/${userId}`);
    const data = await response.json();
    document.getElementById('getUserResult').textContent = JSON.stringify(data, null, 2);
}

async function createUser() {
    const userId = document.getElementById('newUserId').value;
    const userName = document.getElementById('newUserName').value;
    const userEmail = document.getElementById('newUserEmail').value;
    
    const response = await fetch('/create-user', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            user_id: userId,
            name: userName,
            email: userEmail
        }),
    });
    
    const data = await response.json();
    document.getElementById('createUserResult').textContent = JSON.stringify(data, null, 2);

    async function getUser() {
        const userId = document.getElementById('userId').value;
        const response = await fetch(`/get-user/${userId}`);
        const data = await response.json();
        document.getElementById('getUserResult').textContent = JSON.stringify(data, null, 2);
    }
    
    async function createUser() {
        const userId = document.getElementById('newUserId').value;
        const userName = document.getElementById('newUserName').value;
        const userEmail = document.getElementById('newUserEmail').value;
    
        const response = await fetch('/create-user', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                user_id: userId,
                name: userName,
                email: userEmail
            }),
        });
    
        const data = await response.json();
        document.getElementById('createUserResult').textContent = JSON.stringify(data, null, 2);
    }
    
    async function updateUser() {
        const userId = document.getElementById('updateUserId').value;
        const userName = document.getElementById('updateUserName').value;
        const userEmail = document.getElementById('updateUserEmail').value;
    
        const response = await fetch(`/update-user/${userId}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                name: userName,
                email: userEmail
            }),
        });
    
        const data = await response.json();
        document.getElementById('updateUserResult').textContent = JSON.stringify(data, null, 2);
    }

    
    async function deleteUser() {
        const userId = document.getElementById('deleteUserId').value;
    
        const response = await fetch(`/delete-user/${userId}`, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json',
            }
        });
    
        const data = await response.json();
        document.getElementById('deleteUserResult').textContent = JSON.stringify(data, null, 2);
    }


}
