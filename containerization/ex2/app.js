import moment from 'moment';
import axios from 'axios';
import readline from 'readline';

// Create an interface for reading user input
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

// Function to get date input and format it
function getDateInput() {
    rl.question('Enter a date (dd-mm-yyyy): ', (input) => {
        if (input) {
            console.log(`Date given is: ${input}`);
            let input_date = input.split('-').map(num => parseInt(num, 10));

            let obj = {
                year: input_date[2], month: input_date[1] - 1, day: input_date[0] 
            };

            // Format the date using moment
            let formattedDate = moment(obj).format("dddd, Do MMM YYYY");
            console.log(`Formatted date: ${formattedDate}`);

            // Make an API call using axios and log the response
            axios.get('https://jsonplaceholder.typicode.com/todos/1') // Example API URL
                .then(response => {
                    console.log('API response:', formattedDate);
                    rl.close(); // Close the readline interface
                })
                .catch(error => {
                    console.error('Error fetching data from API:', error);
                    rl.close();
                });

        } else {
            console.log('Please provide a valid date in dd-mm-yyyy format');
            rl.close();
        }
    });
}

// Call the function to start the process
getDateInput();
