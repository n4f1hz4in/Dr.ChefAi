const chatLog = document.getElementById('chat-log');
const userInput = document.getElementById('user-input');
const sendButton = document.getElementById('send-button');

// Add a click event listener to the send button
sendButton.addEventListener('click', sendMessage);

// Function to send a user message
function sendMessage() {
    const message = userInput.value.trim();

    // If the message is empty, do nothing
    if (message === '') {
        return;
    }

    // Append the user's message to the chat log
    appendMessage('user', message);
    userInput.value = '';

    // Show the loading view while waiting for the response
    showLoadingView();

    // Configure the fetch options
    const options = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer 4YiXCbrgcb_h1GXyuYhZ_sNrjRrJTh9YDZ_nwq8FUTg', // Replace with your actual API key
        },
        body: JSON.stringify({
            model: 'llama-2-70b-chat',
            messages: [
                {
                    role: 'system',
                    content: 'You are a helpful chef assistant named Dr chefAi'
                },
                {
                    role: 'user',
                    content: message
                }
            ],
            max_tokens: 2000,
            temperature: 0.7,
            n: 1,
            stop: []
        }),
    };

    // Make a fetch request to the API
    fetch('https://api.naga.ac/v1/chat/completions', options)
        .then(response => response.json())
        .then(response => {
            // Log the response to see its structure
            console.log(response);

            // Append the bot's message to the chat log
            appendMessage('bot', response.choices[0].message.content);

            // Hide the loading view after receiving the response
            hideLoadingView();
        })
        .catch(error => {
            console.error('Error:', error);

            // Hide the loading view in case of an error
            hideLoadingView();
        });
}

// Function to append a message to the chat log
function appendMessage(sender, message) {
    const messageElement = document.createElement('div');
    const iconElement = document.createElement('div');
    const chatElement = document.createElement('div');
    const icon = document.createElement('i');

    chatElement.classList.add('chat-box');
    iconElement.classList.add('icon');
    messageElement.classList.add(sender);
    messageElement.innerText = message;

    if (sender === 'user') {
        icon.classList.add('fa-regular', 'fa-user');
        iconElement.setAttribute('id', 'user-icon');
    } else {
        icon.classList.add('fa-solid', 'fa-robot');
        iconElement.setAttribute('id', 'bot-icon');
    }

    iconElement.appendChild(icon);
    chatElement.appendChild(iconElement);
    chatElement.appendChild(messageElement);
    chatLog.appendChild(chatElement);

    // Scroll to the bottom of the chat log
    chatLog.scrollTop = chatLog.scrollHeight;
}

// Get references to the loading view and user input element
const loadingView = document.getElementById('loading-view');

// Function to show the loading view
function showLoadingView() {
    loadingView.style.display = 'block';
}

// Function to hide the loading view
function hideLoadingView() {
    loadingView.style.display = 'none';
}




