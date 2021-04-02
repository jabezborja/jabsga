
function copyText(url) {
    let toolTipText = document.querySelector('.tooltiptext');
    var textToCopy = "https://jabsga.herokuapp.com/"+url;

    var myTemporaryInputElement = document.createElement("input");
    myTemporaryInputElement.type = "text";
    myTemporaryInputElement.value = textToCopy;

    document.body.appendChild(myTemporaryInputElement);
    toolTipText.innerHTML = "Copied!";

    myTemporaryInputElement.select();
    document.execCommand("Copy");

    document.body.removeChild(myTemporaryInputElement);

    setTimeout(function() {toolTipText.innerHTML = "Copy to clipboard"}, 2000);
}