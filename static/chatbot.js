document.addEventListener('DOMContentLoaded', function () {
    const messageInput = document.getElementById('userMessage');
    const messagesDiv = document.getElementById('messages');
    const quickRepliesDiv = document.getElementById('quick-replies');

    // Function to send a message to the server
    function sendMessage() {
        const message = messageInput.value.trim();
        if (message === '') return;

        displayMessage('You: ' + message);
        messageInput.value = '';

        fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message: message })
        })
        .then(response => response.json())
        .then(data => {
            displayMessage('AFFAN: ' + data.response);
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }

    // Function to send a predefined quick reply
    function sendQuickReply(reply) {
        displayMessage('You: ' + reply);

        fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message: reply })
        })
        .then(response => response.json())
        .then(data => {
            displayMessage('AFFAN: ' + data.response);
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }

    // Function to display messages in the chat box
    function displayMessage(message) {
        const messageElement = document.createElement('p');
        messageElement.textContent = message;
        messagesDiv.appendChild(messageElement);
        messagesDiv.scrollTop = messagesDiv.scrollHeight; // Auto-scroll to the bottom
    }

    // Attach event listeners
    document.querySelector('button[onclick="sendMessage()"]').addEventListener('click', sendMessage);
    messageInput.addEventListener('keypress', function(event) {
        if (event.key === 'Enter') {
            event.preventDefault();
            sendMessage();
        }
    });

    // Add quick reply buttons
    const quickReplies = [
        'Tell me about services',
        'How to contact you?',
        'What is your lab about?'
    ];
    
    quickReplies.forEach(reply => {
        const button = document.createElement('button');
        button.textContent = reply;
        button.addEventListener('click', () => sendQuickReply(reply));
        quickRepliesDiv.appendChild(button);
    });
});
