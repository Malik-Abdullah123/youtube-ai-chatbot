async function loadVideo() {

    let id = document.getElementById("videoId").value.trim();

    if (id === "") {
        alert("Please enter YouTube Video ID");
        return;
    }

    let res = await fetch("/load_video", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            video_id: id
        })
    });

    let data = await res.json();

    if (data.status === "success") {
        alert("Video Loaded Successfully!");
        document.getElementById("chatBox").innerHTML = "";
    } else {
        alert(data.message);
    }
}

async function sendMessage() {

    let input = document.getElementById("message");
    let msg = input.value.trim();

    if (msg === "") return;

    let chat = document.getElementById("chatBox");

    // User Message
    chat.innerHTML += `
        <div style="margin:10px 0;">
            <b>You:</b>
            <p>${msg}</p>
        </div>
    `;

    chat.scrollTop = chat.scrollHeight;

    input.value = "";

    try {

        let res = await fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                message: msg
            })
        });

        let data = await res.json();

        // AI Message
        chat.innerHTML += `
            <div style="margin:10px 0;">
                <b>AI:</b>
                <p>${data.answer}</p>
            </div>
            <hr>
        `;

        chat.scrollTop = chat.scrollHeight;

    } catch (err) {

        chat.innerHTML += `
            <div style="color:red;">
                Error: ${err}
            </div>
        `;
    }

}

// Enter key support
document.getElementById("message").addEventListener("keypress", function (event) {

    if (event.key === "Enter") {
        sendMessage();
    }

});