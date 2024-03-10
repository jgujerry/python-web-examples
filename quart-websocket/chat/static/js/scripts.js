
const ws = new WebSocket(`ws://${location.host}/ws`);

ws.addEventListener('message', function (event) {
    const li = document.createElement("li");
    li.appendChild(document.createTextNode(event.data));
    document.getElementById("messages").appendChild(li);
});

function send(event) {
    const message = (new FormData(event.target)).get("message");
    if (message) {
        ws.send(message);
    }
    event.target.reset();
    return false;
}
