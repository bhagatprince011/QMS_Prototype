// Handle file selection and display file names
const fileInput = document.getElementById('formFile');
if (fileInput) {
    let debounceTimer;

    fileInput.addEventListener('change', () => {
        clearTimeout(debounceTimer);  // Clear the previous timer
        debounceTimer = setTimeout(() => {
            const fileList = fileInput.files;
            const fileNames = Array.from(fileList).map(file => file.name);

            // Create a new div to display selected files
            const fileNamesDisplay = document.createElement('div');
            fileNamesDisplay.innerHTML = `<strong>Selected files:</strong><ul>${fileNames.map(file => `<li>${file}</li>`).join('')}</ul>`;
            document.body.appendChild(fileNamesDisplay);
        }, 300);  // Wait 300ms before processing the event
    });
}

// Show a spinner during the upload process
function showSpinner() {
    const spinner = document.createElement('div');
    spinner.classList.add('spinner');  // Add appropriate styling for the spinner
    document.body.appendChild(spinner);
}

function hideSpinner() {
    const spinner = document.querySelector('.spinner');
    if (spinner) {
        spinner.remove();
    }
}

// Handle form submission for file upload
document.getElementById('uploadForm').addEventListener('submit', function(event) {
    event.preventDefault();  // Prevent the default form submission (page reload)

    showSpinner();  // Show spinner when the upload starts

    // Create a FormData object from the form
    const formData = new FormData(this);  // 'this' refers to the form element

    // Use fetch to send the form data via AJAX to the server
    fetch('/qms_app/upload/', {
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
        },
    })
    .then(response => response.json())  // Parse JSON response from the server
    .then(data => {
        hideSpinner();  // Hide spinner when done
        if (data.success) {
            // If success, display success message
            showAlert('success', 'File uploaded successfully!');
        } else {
            // If failure, display error message
            showAlert('error', 'Failed to upload file!');
        }
    })
    .catch(error => {
        hideSpinner();  // Hide spinner if an error occurs
        // Handle any errors in the fetch request
        showAlert('error', 'An error occurred while uploading the file.');
    });
});

// Function to show success or error messages
function showAlert(type, message) {
    const alertBox = document.createElement('div');
    alertBox.classList.add('alert');
    alertBox.classList.add(type === 'success' ? 'alert-success' : 'alert-danger');
    alertBox.innerHTML = message;

    document.body.appendChild(alertBox);

    // Auto-close the alert box after 3 seconds
    setTimeout(() => {
        alertBox.remove();
    }, 3000);
}

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
