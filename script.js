function convert() {
    const result = document.getElementById("result"); 
    const url = document.getElementById("url").value.trim();

    if (!url) {
        result.textContent = "Error: Please enter a website.";
        result.style.color = "red";
        return;
    }

    // Send request to Flask backend
    fetch(`https://sachacks-1.onrender.com/check?url=${encodeURIComponent(url)}`)
        .then(response => response.json())
        .then(data => {
            console.log("API Response:", data);
            if (data.error) {
                result.textContent = "Error: " + data.error;
                result.style.color = "red";
            } else {
                result.innerHTML = `
                    <strong>Website:</strong> ${data.url} <br>
                    <strong>GPT Analysis:</strong> ${data.gpt_analysis}
                `;
                result.style.color = "white";
            }
        })
        .catch(error => {
            result.textContent = "Error fetching data.";
            result.style.color = "red";
            console.error("Fetch error:", error);
        });
}