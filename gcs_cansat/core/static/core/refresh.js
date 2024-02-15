const refreshTimer = document.getElementById('refresh-timer');
let timerInSeconds = 0;
setInterval(() => {
timerInSeconds += 1;

if (timerInSeconds >= 2) {
    window.location.reload();}
    },1000);