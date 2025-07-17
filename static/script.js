async function sendMessage() {
    const userInput = document.getElementById("user-input").value;
    if (!userInput) return;

    const chatBox = document.getElementById("chat-box");

    // Show user message
    chatBox.innerHTML += `<div class="user-message">👤 ${userInput}</div>`;

    // Clear input field
    document.getElementById("user-input").value = "";

    // Send to backend
    const response = await fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: userInput })
    });

    const data = await response.json();

    // Show AI response
    chatBox.innerHTML += `<div class="ai-message">🤖 ${data.reply}</div>`;
    chatBox.scrollTop = chatBox.scrollHeight;
}
