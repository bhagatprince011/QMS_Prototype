// Handle form submission for file upload
document.getElementById('uploadForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission (page reload)

    // Show spinner and disable the screen
    const spinner = document.createElement("div");
    spinner.id = "spinner";
    spinner.style.position = "fixed";
    spinner.style.top = "0";
    spinner.style.left = "0";
    spinner.style.width = "100%";
    spinner.style.height = "100%";
    spinner.style.backgroundColor = "rgba(0, 0, 0, 0.5)";
    spinner.style.zIndex = "9999";
    spinner.style.display = "flex";
    spinner.style.justifyContent = "center";
    spinner.style.alignItems = "center";
    spinner.innerHTML = '<div class="spinner-border text-light" role="status"><span class="sr-only">Loading...</span></div>';
    document.body.appendChild(spinner);

    // Create a FormData object from the form
    const formData = new FormData(this); // 'this' refers to the form element

    // Use fetch to send the form data via AJAX to the server
    fetch('/qms_app/upload/', {
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
        },
    })
        .then(response => response.json()) // Parse JSON response from the server
        .then(data => {
            if (data.success) {
                // If success, display success message
                alert('File uploaded successfully!');
            } else {
                // If failure, display error message
                alert('Failed to upload file!');
            }
        })
        .catch(error => {
            // Handle any errors in the fetch request
            alert('An error occurred while uploading the file.');
        })
        .finally(() => {
            // Remove spinner after upload
            if (spinner) {
                document.body.removeChild(spinner);
                    // Clear the file input and reset the form
                document.getElementById('uploadForm').reset();
            }
        });

});

// Ensure the card heights are consistent
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
