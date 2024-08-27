

function displayTime() {
  const now = new Date();
  const time = now.toLocaleTimeString('en-US', {
      hour: '2-digit',
      minute: '2-digit',
      second: '2-digit',
      hour12: false 
  });
  document.getElementById('clock').textContent = time;
}


function toggle()
{
    const container = document.getElementById("container");
    container.classList.toggle("dark-container");
    // Assuming you have a reference to the button element
    const button = document.querySelector('button');

// Toggle the text content based on the current text
if (button.textContent === 'Change to Light mode') {
  button.textContent = 'Change to Dark mode';
} else {
  button.textContent = 'Change to Light mode';
}

    const clock = document.getElementById("clock");
    clock.classList.toggle("dark-clock");
}

setInterval(displayTime,1000);

displayTime();