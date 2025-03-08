const roomName = "{{ room_name }}";
const username = "{{ username }}";
const socket = new WebSocket(`ws://127.0.0.1:8000/ws/chat/${roomName}/`);

socket.onopen = () => console.log("Connected to WebSocket");

socket.onmessage = function(event) {
    const data = JSON.parse(event.data);
    const chatBox = document.getElementById("chat-box");
    chatBox.innerHTML += `<p><strong>${data.username}:</strong> ${data.message}</p>`;
};

document.getElementById("send-button").onclick = function() {
    const messageInput = document.getElementById("message-input");
    const message = messageInput.value;
    socket.send(JSON.stringify({
        username: username,
        message: message
    }));
    messageInput.value = "";
};
