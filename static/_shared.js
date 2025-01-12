function startSpinner() {
    
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


}

function stopSpinner() {
    document.body.removeChild(spinner);
}