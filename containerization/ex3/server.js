const express = require('express');
const app = express();

// Use the PORT from the environment variables, or default to 3000
const PORT = process.env.PORT || 3000;

app.get('/', (req, res) => {
    res.json({ message: `Server is running on port ${PORT}` }); // Sending JSON response
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
