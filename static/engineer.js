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