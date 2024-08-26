document.getElementById('search-button').addEventListener('click', async function() {
    const query = document.getElementById('search-input').value;
    const apiKey = '262e0edd'; // Replace with your OMDb API key
    const url = `http://www.omdbapi.com/?apikey=${apiKey}&s=${encodeURIComponent(query)}`;

    try {
        const response = await fetch(url);
        const data = await response.json();
        const movieList = document.getElementById('main');
        movieList.innerHTML = ''; // Clear previous results

        if (data.Response === 'True') {
            const sortedMovies = data.Search.sort((a, b) => {
                return parseInt(b.Year) - parseInt(a.Year);
            });
            const moviesPerPage = 3; // Number of movies to show per load
            let currentIndex = 0;
            const loadMoreButton = document.getElementById('load-more-button');

            const loadMovies = () => {
                

           // loadMoreButton.style.display = 'none'; // Hide initially
                const nextMovies = sortedMovies.slice(currentIndex, currentIndex + moviesPerPage);
                console.log("next movies:",nextMovies);
                nextMovies.forEach(movie => {
                    const cardDiv = document.createElement('div');
                    cardDiv.className = 'card';
                    cardDiv.setAttribute('data-id', movie.imdbID);

                    const description = document.createElement('h1');
                    description.innerHTML = `${movie.Title} (${movie.Year})`;
                    cardDiv.appendChild(description);

                    const img = document.createElement('img');
                    img.src = movie.Poster !== 'N/A' ? movie.Poster : 'path/to/default-image.png';
                    img.alt = movie.Title;
                    img.style.width = '100%';
                    img.style.height= '500px';
                    cardDiv.appendChild(img);

                    movieList.appendChild(cardDiv);

                    cardDiv.addEventListener('click', async function() {
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
            };

            loadMovies(); // Load initial set of movies

            loadMoreButton.addEventListener('click', loadMovies); // Load more on button click

        } else {
            movieList.innerHTML = '<h1>No results found</h1>';
        }
    } catch (error) {
        console.error('Error fetching data:', error);
    }
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
                    Actors: movieActors, Plot: moviePlot, Poster: moviePoster, Language:movieLanguage, Ratings:movieRatings } = movieDetails;
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
