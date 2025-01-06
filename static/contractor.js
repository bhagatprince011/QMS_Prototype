// Handle file selection and display file names
const fileInput = document.getElementById('formFile');
if (fileInput) {
    fileInput.addEventListener('change', () => {
        const fileList = fileInput.files;
        const fileNames = Array.from(fileList).map(file => file.name);
        alert(`Selected files: \n${fileNames.join('\n')}`);
    });
}

// Handle form submission for file upload
document.getElementById('uploadForm').addEventListener('submit', function(event) {
    event.preventDefault();  // Prevent the default form submission (page reload)

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
        if (data.success) {
            // If success, display success message
            showAlert('success', 'File uploaded successfully!');
        } else {
            // If failure, display error message
            showAlert('error', 'Failed to upload file!');
        }
    })
    .catch(error => {
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

// Function to show success or error messages in an alert box
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
