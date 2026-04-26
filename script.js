async function sendMsg() {
    let input = document.getElementById("msg");
    let text = input.value.trim();

    if (!text) return;

    let chat = document.getElementById("chat");

    // show user message
    chat.innerHTML += `<div class="msg user">You: ${text}</div>`;

    input.value = "";

    try {
        let res = await fetch("http://127.0.0.1:5000/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message: text })
        });

        let data = await res.json();

        // ✅ IMPORTANT FIX
        let reply = data.response;

        // fallback safety
        if (!reply) {
            reply = "No response from bot";
        }

        chat.innerHTML += `<div class="msg bot">Bot: ${reply}</div>`;

        chat.scrollTop = chat.scrollHeight;

    } catch (error) {
        console.log(error);
        chat.innerHTML += `<div class="msg bot">❌ Backend not responding</div>`;
    }
}