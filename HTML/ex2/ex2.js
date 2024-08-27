

function displayTime()
{
    const now = new Date();
    const hours=now.getHours().toString().padStart(2.0);
    const mins=now.getMinutes().toString().padStart(2,0);
    const secs=now.getSeconds().toString().padStart(2,0);
    const time=`${hours}:${mins}:${secs}`;
    document.getElementById('clock').textContent=time;
    


}

function toggle()
{
    var element = document.getElementById("container");
    element.classList.toggle("dark-container");
    // Assuming you have a reference to the button element
const button = document.querySelector('button');

// Toggle the text content based on the current text
if (button.textContent === 'Change to Light mode') {
  button.textContent = 'Change to Dark mode';
} else {
  button.textContent = 'Change to Light mode';
}

    var element2 = document.getElementById("clock");
    element2.classList.toggle("dark-clock");
}

setInterval(displayTime,1000);

displayTime();