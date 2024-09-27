import moment from 'moment';
import axios from 'axios';
import readline from 'readline';

// Create an interface for reading user input
const readLine_interface = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

API_URL='https://jsonplaceholder.typicode.com/todos/1'

// Function to get date input and format it
function getDateInput() {
    readLine_interface.question('Enter a date (dd-mm-yyyy): ', (input) => {
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
            axios.get(API_URL) // Example API URL
                .then(response => {
                    console.log('API response:', response.data);
                    readLine_interface.close(); // Close the readline interface
                })
                .catch(error => {
                    console.error('Error fetching data from API:', error);
                    readLine_interface.close();
                });

        } else {
            console.log('Please provide a valid date in dd-mm-yyyy format');
            readLine_interface.close();
        }
    });
}

// Call the function to start the process
getDateInput();
