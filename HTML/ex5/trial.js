
const apiKey = 'http://www.omdbapi.com/?i=tt3896198&apikey=262e0edd'; // Replace with your OMDb API key
let currentPage = 1;
let movieData = [];

const fetchMovies = async (page = 1) => {
    try {
        const response = await fetch(`https://www.omdbapi.com/?s=batman&apikey=${apiKey}&page=${page}`);
        const data = await response.json();
        if (data.Response === 'True') {
            movieData = [...movieData, ...data.Search];
            displayMovies(movieData);
        }
    } catch (error) {
        console.error('Error fetching movies:', error);
    }
};

const displayMovies = (movies) => {
    const movieCards = document.getElementById('movie-cards');
    movieCards.innerHTML = '';

    movies.forEach((movie) => {
        const card = `
            <div class="movie-card">
                <div class="movie-poster">
                    <img src="${movie.Poster}" alt="${movie.Title}">
                </div>
                <div class="movie-info">
                    <div class="movie-title">${movie.Title}</div>
                    <div class="movie-meta">${movie.Year} | ${movie.Type}</div>
                    <button onclick="viewDetails('${movie.imdbID}')">View Details</button>
                </div>
            </div>
        `;
        movieCards.insertAdjacentHTML('beforeend', card);
    });
};

const viewDetails = async (imdbID) => {
    try {
        const response = await fetch(`https://www.omdbapi.com/?i=${imdbID}&apikey=${apiKey}&plot=full`);
        const movie = await response.json();
        const iframe = document.getElementById('movie-details');
        iframe.style.display = 'block';
        iframe.srcdoc = `
            <h2>${movie.Title}</h2>
            <p><strong>Year:</strong> ${movie.Year}</p>
            <p><strong>Rated:</strong> ${movie.Rated}</p>
            <p><strong>Released:</strong> ${movie.Released}</p>
            <p><strong>Runtime:</strong> ${movie.Runtime}</p>
            <p><strong>Genre:</strong> ${movie.Genre}</p>
            <p><strong>Director:</strong> ${movie.Director}</p>
            <p><strong>Actors:</strong> ${movie.Actors}</p>
            <p><strong>Plot:</strong> ${movie.Plot}</p>
            <p><strong>Languages:</strong> ${movie.Language}</p>
            <h3>Ratings:</h3>
            ${movie.Ratings.map(rating => `<p>${rating.Source}: ${rating.Value}</p>`).join('')}
        `;
    } catch (error) {
        console.error('Error fetching movie details:', error);
    }
};

document.getElementById('sort-year').addEventListener('click', () => {
    movieData.sort((a, b) => parseInt(b.Year) - parseInt(a.Year));
    displayMovies(movieData);
});

document.getElementById('search').addEventListener('input', (event) => {
    const searchQuery = event.target.value.toLowerCase();
    const filteredMovies = movieData.filter(movie =>
        movie.Title.toLowerCase().includes(searchQuery)
    );
    displayMovies(filteredMovies);
});

document.getElementById('load-more').addEventListener('click', () => {
    currentPage++;
    fetchMovies(currentPage);
});

window.onload = () => fetchMovies();
