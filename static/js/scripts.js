document.getElementById('summarize-form').addEventListener('submit', function(e) {
    e.preventDefault();
    const content = document.getElementById('content').value;
    fetch('/summarize', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: new URLSearchParams({
            'content': content
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            document.getElementById('result').innerText = `Error: ${data.error}`;
        } else {
            document.getElementById('result').innerText = data.summary;
        }
    });
});
