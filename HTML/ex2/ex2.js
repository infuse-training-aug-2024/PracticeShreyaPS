

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
    var element2 = document.getElementById("clock");
    element2.classList.toggle("dark-clock");
}

setInterval(displayTime,1000);

displayTime();