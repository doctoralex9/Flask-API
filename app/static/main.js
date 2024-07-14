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
