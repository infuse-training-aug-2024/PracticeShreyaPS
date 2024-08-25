const apiKey = '262e0edd'; // Your API key
const movieTitle = 'Inception'; // Example movie title

const fetchMovieData = async (title) => {
    try {
        const response = await fetch(`http://www.omdbapi.com/?apikey=${apiKey}&t=${encodeURIComponent(title)}`);
        const data = await response.json();

        if (data.Response === 'True') {
            console.log('Movie Data:', data);
            // You can now use the data object to display the movie information
        } else {
            console.error('Error:', data.Error);
        }
    } catch (error) {
        console.error('Fetch error:', error);
    }
};

// Fetch movie data for the specified title
fetchMovieData(movieTitle);




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
