function convert() {
    const result = document.getElementById("result"); 
    const url = document.getElementById("url").value.trim();

    if (!url) {
        result.textContent = "Error: Please enter a website.";
        result.style.color = "red";
        return;
    }

    // Send request to Flask backend
    fetch(`https://corsproxy.io/?${encodeURIComponent("https://sachacks-backend.onrender.com/check?url=" + url)}`)
        .then(response => response.json())
        .then(data => {
            console.log("API Response:", data); // Debugging: Log API response

            if (data.error) {
                result.textContent = "Error: " + data.error;
                result.style.color = "red";
            } else if (data.statistics && data.statistics.co2) {
                // ✅ Display carbon emissions result
                result.innerHTML = `
                    <strong>Website:</strong> ${data.url} <br>
                    <strong>Carbon Emissions:</strong> ${data.statistics.co2.grid.grams}g CO2 per visit <br>
                    <strong>Rating:</strong> ${data.rating} <br>
                    <strong>Greener Than:</strong> ${Math.round(data.cleanerThan * 100)}% of tested sites
                `;
                result.style.color = "white"; // Keep it readable
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