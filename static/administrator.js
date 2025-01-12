
document.addEventListener("DOMContentLoaded", () => {
    const cards = document.querySelectorAll(".card");
    let maxHeight = 0;
  
    // Find the maximum height of all cards
    cards.forEach(card => {
      maxHeight = Math.max(maxHeight, card.offsetHeight);
    });
  
    // Apply the maximum height to all cards
    cards.forEach(card => {
      card.style.height = maxHeight + "px";
    });
});


document.getElementById("downloadProofsButton").addEventListener("click", function (event) {
    event.preventDefault();  // Prevent default anchor behavior (no page reload)
  
    const roadId = document.getElementById('road_id').value  // Assuming you have the road ID available in the template
    startSpinner(); // Show spinner while downloading file
    
    // Perform a fetch request to the downloadEvidence view
    fetch(`/qms_app/download-evidence/${roadId}/`)
    .then(response => {
        const contentType = response.headers.get("Content-Type");
        if (contentType && contentType.includes("application/json")) {
            // Handle JSON response
            return response.json().then(data => {
                if (data.success) {
                    alert("Unexpected success in JSON response!"); // This shouldn't happen
                } else {
                    alert(data.message); // Show the error message
                }
            });
        } else {
            // Handle binary file response
            response.blob().then(blob => {
                const url = window.URL.createObjectURL(blob);
                const a = document.createElement("a");
                a.style.display = "none";
                a.href = url;
  
                // Use the file name from the response headers if available
                const contentDisposition = response.headers.get("Content-Disposition");
                let fileName = "downloaded_file";
                if (contentDisposition) {
                    const fileNameMatch = contentDisposition.match(/filename="(.+)"/);
                    if (fileNameMatch.length > 1) {
                        fileName = fileNameMatch[1];
                    }
                }
                a.download = fileName;
                document.body.appendChild(a);
                a.click();
                window.URL.revokeObjectURL(url);
            });
            spinner = document.getElementById('spinner');
            if (spinner) {
                stopSpinner();
            }
        }
    })
    .catch(error => {
        alert("An error occurred: " + error.message); // Show error for network issues
    });
  });
  