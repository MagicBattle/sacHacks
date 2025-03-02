function convert() {
    const result = document.getElementById("result"); 
    const url = document.getElementById("url").value.trim();

    if (!url) {
        result.textContent = "Error: Please enter a website.";
        result.style.color = "red";
        return;
    }

    // Call your Flask backend, which acts as a proxy
    fetch(`https://sachacks-1.onrender.com/check?url=${encodeURIComponent(url)}`)
        .then(response => response.json())
        .then(data => {
            console.log("API Response:", data);
            if (data.error) {
                result.textContent = "Error: " + data.error;
                result.style.color = "red";
            } else if (data.statistics && data.statistics.co2) {
                result.innerHTML = `
                    <strong>Website:</strong> ${data.url} <br>
                    <strong>Carbon Emissions:</strong> ${data.statistics.co2.grid.grams}g CO2 per visit <br>
                    <strong>Rating:</strong> ${data.green ? "Green Hosted ✅" : "Not Green ❌"} <br>
                    <strong>Greener Than:</strong> ${Math.round(data.cleanerThan * 100)}% of tested sites
                `;
                result.style.color = "white";
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