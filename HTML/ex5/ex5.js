let sortOption = 'ascending'; // Default sort option
let currentIndex = 0; // Keep track of the current index globally
let sortedMovies = []; // Store sorted movies globally
const moviesPerPage = 3; // Number of movies to show per load

document.addEventListener("DOMContentLoaded", async function () {
    const apiKey = '262e0edd'; // Replace with your OMDb API key
    const url = `http://www.omdbapi.com/?apikey=${apiKey}&s=${encodeURIComponent('blade')}`;
    await getMovies(url, sortOption);
});

const sortSelect = document.getElementById('sort');
sortSelect.addEventListener('change', async () => {
    sortOption = sortSelect.value;
    console.log(sortOption);
    query = document.getElementById('search-input').value || 'blade';
    const apiKey = '262e0edd'; // Replace with your OMDb API key
    const url = `http://www.omdbapi.com/?apikey=${apiKey}&s=${encodeURIComponent(query)}`;
    await getMovies(url, sortOption);
});

document.getElementById('search-button').addEventListener('click', async function () {
    query = document.getElementById('search-input').value;
    const apiKey = '262e0edd'; // Replace with your OMDb API key
    const url = `http://www.omdbapi.com/?apikey=${apiKey}&s=${encodeURIComponent(query)}`;
    await getMovies(url, sortOption);
});

async function handleCardClick(movieId) {
    const apiKey = '262e0edd'; // Replace with your OMDb API key
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
        const data = await response.json();
        const movieList = document.getElementById('main');
        movieList.innerHTML = ''; // Clear previous results

        if (data.Response === 'True') {
            currentIndex = 0; // Reset index for a new search
            sortedMovies = await sortMovie(data, sortOption);

            loadMovies(); // Load initial set of movies
        } else {
            movieList.innerHTML = '<h1>No results found</h1>';
        }
    } catch (error) {
        console.error('Error fetching data:', error);
    }
}

function loadMovies() {
    const movieList = document.getElementById('main');
    const loadMoreButton = document.getElementById('load-more-button');

    const nextMovies = sortedMovies.slice(currentIndex, currentIndex + moviesPerPage);
    console.log("sorted movies", sortedMovies);
    console.log("next movies:", nextMovies);
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
        loadMoreButton.style.display = 'none'; // Hide button when all movies are loaded
    } else {
        loadMoreButton.style.display = 'block'; // Show button
    }
}

// Attach the event listener only once, outside the getMovies function
document.getElementById('load-more-button').addEventListener('click', loadMovies);

async function sortMovie(data, option) {
    let sortedMovies;

    if (option === "ascending") {
        sortedMovies = data.Search.sort((a, b) => {
            return parseInt(a.Year) - parseInt(b.Year);
        });
    } else {
        sortedMovies = data.Search.sort((a, b) => {
            return parseInt(b.Year) - parseInt(a.Year);
        });
    }

    return sortedMovies;
}
