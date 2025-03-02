function convert() {
    const result = document.getElementById("result"); 
    const url = document.getElementById("url").value.trim();

    if (!url) {
        result.textContent = "Error: Please enter a website.";
        result.style.color = "red";
        return;
    }

    fetch(`http://127.0.0.1:5000/check?url=${encodeURIComponent(url)}`)
        .then(response => response.json())
        .then(data => {
            console.log("API Response:", data); // Debugging: Log API response

            if (data.error) {
                result.textContent = "Error: " + data.error;
                result.style.color = "red";
            } else if (data.statistics && data.statistics.co2) {
                // ✅ Check if `data.statistics.co2` exists before using it # LMAO
                result.textContent = `Carbon Emissions: ${data.statistics.co2}g CO2 per visit`;
                result.style.color = "green";
            } else {
                result.textContent = "No carbon footprint data available.";
                result.style.color = "orange";
            }
        })
        .catch(error => {
            result.textContent = "Error fetching data.";
            result.style.color = "red";
            console.error("Fetch error:", error);
        });
}