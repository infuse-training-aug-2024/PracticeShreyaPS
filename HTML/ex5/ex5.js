let sortOption = 'ascending'; // Default sort option
let currentIndex = 0; // used for load more function
let sortedMovies = []; // Stores sorted movies globally
const moviesPerPage = 3; // Number of movies to show per load
const apiKey = '262e0edd'; // api key

document.addEventListener("DOMContentLoaded", async function () { // to load default movie results
    const url = `http://www.omdbapi.com/?apikey=${apiKey}&s=${encodeURIComponent('blade')}`;
    await getMovies(url, sortOption);
});

const sortSelect = document.getElementById('sort');
sortSelect.addEventListener('change', async () => { //implementing sort by year
    sortOption = sortSelect.value;
    let query = document.getElementById('search-input').value || 'blade';
    const url = `http://www.omdbapi.com/?apikey=${apiKey}&s=${encodeURIComponent(query)}`;
    await getMovies(url, sortOption);
});

document.getElementById('search-button').addEventListener('click', async function () { //passing query for search input
    query = document.getElementById('search-input').value;
    const url = `http://www.omdbapi.com/?apikey=${apiKey}&s=${encodeURIComponent(query)}`;
    await getMovies(url, sortOption);
});

async function handleCardClick(movieId) { // to display i frame contents on card click
    const url = `http://www.omdbapi.com/?apikey=${apiKey}&i=${encodeURIComponent(movieId)}&plot=full`;

    try {
        const response = await fetch(url);
        const movieDetails = await response.json();

        if (movieDetails.Response === 'True') {
            const { Title: movieTitle, Year: movieYear, Rated: movieRated, Released: movieRelease,
                Runtime: movieRunTime, Genre: movieGenre, Director: movieDirector,
                Actors: movieActors, Plot: moviePlot, Poster: moviePoster, Language: movieLanguage, Ratings: movieRatings } = movieDetails;
            const ratingsString = movieRatings.map(rating => `${rating.Source}: ${rating.Value}`).join(', ');

            const iframe = document.getElementById('movie-iframe');
            iframe.src = `details.html?title=${encodeURIComponent(movieTitle)}&year=${encodeURIComponent(movieYear)}&id=${encodeURIComponent(movieId)}
            &rated=${encodeURIComponent(movieRated)}&release=${encodeURIComponent(movieRelease)}&runtime=${encodeURIComponent(movieRunTime)}
            &genre=${encodeURIComponent(movieGenre)}&director=${encodeURIComponent(movieDirector)}&actors=${encodeURIComponent(movieActors)}
            &plot=${encodeURIComponent(moviePlot)}&poster=${encodeURIComponent(moviePoster)}
            &language=${encodeURIComponent(movieLanguage)}&ratings=${encodeURIComponent(ratingsString)}`;
        } else {
            console.error('Error fetching movie details:', movieDetails.Error);
        }
    } catch (error) {
        console.error('Error fetching movie details:', error);
    }
}

async function getMovies(url, sortOption) {
    try {
        const response = await fetch(url);
        const movieData = await response.json();
        const movieList = document.getElementById('main');
        movieList.innerHTML = ''; // Clear previous results

        if (movieData.Response === 'True') {
            currentIndex = 0; // Reset index for a new search
            sortedMovies = await sortMovie(movieData, sortOption);

            loadMovies(); // Load initial set of movies
        } else {
            movieList.innerHTML = '<h1 class="no-results">No results found</h1>';
        }
    } catch (error) {
        console.error('Error fetching movieData:', error);
    }
}

function loadMovies() { // loads content based on inputs
    const movieList = document.getElementById('main');
    const loadMoreButton = document.getElementById('load-more-button');

    const nextMovies = sortedMovies.slice(currentIndex, currentIndex + moviesPerPage);
    nextMovies.forEach(movie => {
        const cardDiv = document.createElement('div');
        cardDiv.className = 'card';
        cardDiv.style.marginTop = '10px';
        cardDiv.setAttribute('data-id', movie.imdbID);

        const description = document.createElement('h1');
        description.innerHTML = `${movie.Title} (${movie.Year})`;
        description.style.alignContent = 'center';
        cardDiv.appendChild(description);

        const img = document.createElement('img');
        img.src = movie.Poster !== 'N/A' ? movie.Poster : 'path/to/default-image.png';
        img.alt = movie.Title;
        img.style.width = '100%';
        img.style.height = '300px';
        cardDiv.appendChild(img);

        const overlay = document.createElement('div');
        overlay.className = 'overlay';
        const overlayText = document.createElement('div');
        overlayText.className = 'overlay-text';
        overlayText.textContent = "Click to see more";
        overlay.style.fontStyle = "oblique";
        overlay.appendChild(overlayText);
        cardDiv.appendChild(overlay);

        movieList.appendChild(cardDiv);

        cardDiv.addEventListener('click', async function () {
            const movieId = this.getAttribute('data-id');
            await handleCardClick(movieId);
        });
    });

    currentIndex += moviesPerPage;

    if (currentIndex >= sortedMovies.length) {
        loadMoreButton.style.display = 'none'; 
    } else {
        loadMoreButton.style.display = 'block'; 
    }
}

document.getElementById('load-more-button').addEventListener('click', loadMovies); //attached outside get movies 

async function sortMovie(movieData, option) { //sorts movies
    let sortedMovies;

    if (option === "ascending") {
        sortedMovies = movieData.Search.sort((a, b) => {
            return parseInt(a.Year) - parseInt(b.Year);
        });
    } else {
        sortedMovies = movieData.Search.sort((a, b) => {
            return parseInt(b.Year) - parseInt(a.Year);
        });
    }

    return sortedMovies;
}
