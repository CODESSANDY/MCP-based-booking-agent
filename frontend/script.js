document.getElementById("send-btn").addEventListener("click", async () => {
  const input = document.getElementById("user-input").value;
  appendMessage("user", input);
  const response = await fetch("http://localhost:8000/search", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({ query: input })
  });
  const data = await response.json();
  appendMessage("agent", data.result);
});

function appendMessage(sender, text) {
  const chatBox = document.getElementById("chat-box");
  const msg = document.createElement("div");
  msg.className = sender;
  msg.textContent = text;
  chatBox.appendChild(msg);
  chatBox.scrollTop = chatBox.scrollHeight;
}
