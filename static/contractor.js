// Handle form submission for file upload
document.getElementById('uploadForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission (page reload)

    // Show spinner and disable the screen
    startSpinner();

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
        .then(data => { console.log(data);
            if (data.success==true) {
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
            spinner = document.getElementById('spinner');
            if (spinner) {
                stopSpinner();
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
