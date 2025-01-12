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

  function toggleButtons() {
    console.log('Toggle buttons');
    // Get references to the radio buttons and the action buttons
    const messageRadio = document.getElementById('inlineRadio1');
    const approvalRadio = document.getElementById('inlineRadio2');
    const sendButton = document.getElementById('sendButton');
    const approveButton = document.getElementById('approveButton');

    // Enable/disable buttons based on selected radio button
    if (messageRadio.checked) {
        sendButton.disabled = false;
        approveButton.disabled = true;
    } else if (approvalRadio.checked) {
        sendButton.disabled = true;
        approveButton.disabled = false;
    }
}

document.getElementById("downloadProofsButton").addEventListener("click", function (event) {
  event.preventDefault();  // Prevent default anchor behavior (no page reload)
  startSpinner(); // Show spinner while downloading file

  const roadId = document.getElementById('road_id').value  // Assuming you have the road ID available in the template
  
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
      }
  })
  .catch(error => {
      alert("An error occurred: " + error.message); // Show error for network issues
  })
  .finally(() => {
    // Remove spinner after upload
        spinner = document.getElementById('spinner');
        if (spinner) {
            document.body.removeChild(spinner);
        }
    });
});


document.getElementById('remarkOrApprove').addEventListener('submit', function(event) {
  event.preventDefault(); // Prevent the default form submission (page reload)

 // Show spinner and disable the screen
  startSpinner();

  const messageRadio = document.getElementById('inlineRadio1');
  const approvalRadio = document.getElementById('inlineRadio2');

  if (messageRadio.checked) {
      
      const formData = new FormData(this);

      // Use fetch to send the form data via AJAX to the server
      fetch('/qms_app/sendRemarks/', {
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
        },
      })
        .then(response => response.json()) // Parse JSON response from the server
        .then(data => {;
            if (data.success==true) {
                // If success, display success message
                alert(data.message);
            } else {
                // If failure, display error message
                alert('Failed to send message! \n' + data.message);
            }
        })
        .catch(error => {
            // Handle any errors in the fetch request
            alert('An error occurred while saving the message.');
        })
        .finally(() => {
            // Remove spinner after upload
            spinner = document.getElementById('spinner');
            if (spinner) {
                document.body.removeChild(spinner);
                    // Clear the file input and reset the form
                document.getElementById('remarksTextarea').value = '';
            }
        });
  }
  else if (approvalRadio.checked) {    
      const formData = new FormData(this); // 'this' refers to the form element

      // Use fetch to send the form data via AJAX to the server
      fetch('/qms_app/approve/', {
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
        },
      })
        .then(response => response.json()) // Parse JSON response from the server
        .then(data => {;
            if (data.success==true) {
                // If success, display success message
                alert(data.message);
            } else {
                // If failure, display error message
                alert('Failed to approve! \n' + data.message);
            }
        })
        .catch(error => {
            // Handle any errors in the fetch request
            alert('An error occurred while Approving.');
        })
        .finally(() => {
            // Remove spinner after upload
            if (spinner) {
                document.body.removeChild(spinner); 
                location.reload();                               
            }
        });
  }

});