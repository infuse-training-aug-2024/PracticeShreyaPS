const toggleButton = document.getElementById('toggle-button');
const sidePanel = document.getElementById('side-panel');
const iframe = document.getElementById('content-iframe');
const mainContent = document.getElementById('main');
toggleButton.addEventListener('click', () => {
    sidePanel.classList.toggle('open');
    toggleButton.textContent = sidePanel.classList.contains('open') ? 'Close Panel' : 'Open Panel';
});

// Optional: Load content in the iframe when opening
sidePanel.addEventListener('transitionend', () => {
    if (sidePanel.classList.contains('open') && !iframe.src) {
        iframe.src = 'https://media.geeksforgeeks.org/wp-content/uploads/20240206111438/uni2.html'; // Replace with your desired URL
    }
});
