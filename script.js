// URL of the API endpoint
const apiURL = "https://api.websitecarbon.com/";



async function fetchData(data) {
    const container = document.getElementById('data-container');
    container.innerHTML = ' ';

    try {
        const response = await fetch(apiURL);

        if(!response.ok) {
            throw new Error("Could not fetch resource");
        }

        const data = await response.json();
        console.log(data);
    } catch(error) {
        console.log(error)
    }

}

// Use the fetch function to make an HTTP request to fetch resources
fetch(apiURL)
   .then(response => {
    if(!response.ok) {
        // Check if the request was successful
        throw new Error("Could not fetch resource");
    }

    // Parse the JSON data from the response
    return response.json();
   })
   .then(data => {
     // Handle the data from the API
     console.log(data);
   })
   .catch(error => {
     // Handle any errors that occurred during the fetch
     console.log("There was an error with the fetch operation: ", error);
   })
