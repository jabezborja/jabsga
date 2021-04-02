// Redirect
var countDown = document.getElementById("countdown");
let count = 4;

function count_decrement(url) {
    if (count == 1) {
        window.location.href = url;
        return;
    }
    
    count--;
    countDown.innerHTML = count;

    setTimeout(count_decrement, 1000, url);
}

function start_count(url) {
    setTimeout(count_decrement, 1000, url);
}