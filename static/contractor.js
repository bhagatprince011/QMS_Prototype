const fileInput = document.getElementById('formFile');
if (fileInput) {
    fileInput.addEventListener('change', () => {
        const fileList = fileInput.files;
        const fileNames = Array.from(fileList).map(file => file.name);
        alert(`Selected files: \n${fileNames.join('\n')}`);
    });
}


const form = document.querySelector('form');
form.addEventListener('submit', (event) => {
    const files = fileInput.files;
    const validExtensions = ['pdf', 'jpg', 'jpeg', 'png', 'gif', 'bmp'];

    for (let file of files) {
        const extension = file.name.split('.').pop().toLowerCase();
        if (!validExtensions.includes(extension)) {
            alert(`Invalid file type: ${file.name}`);
            event.preventDefault();
            return;
        }
    }
});

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

 