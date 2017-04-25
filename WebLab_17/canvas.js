function drag() {
    bear = document.getElementById("bear");
    leftBox = document.getElementById("leftbox");

    bear.addEventListener("dragstart", startDrag, false);
    bear.addEventListener("dragend", endDrag, false);

    leftBox.addEventListener("dragenter", dragEnter, false);
    leftBox.addEventListener("dragleave", dragLeave, false);
    leftBox.addEventListener("dragover", function(e){e.preventDefault()}, false);
    leftBox.addEventListener("drop", drop, false);
}

function startDrag(e) {
    var pic = ' <img id = "bear" src = "http://www.wikiality.com/file/2016/11/bears1.jpg">';
    e.dataTransfer.setData('Picture', pic);
}

function dragEnter(e) {
    e.preventDefault();
    leftBox.style.background = "#3C805D";
    leftBox.style.border = "3px solid black";

}

function dragLeave(e) {
    e.preventDefault();
    leftBox.style.background = "white";
    leftBox.style.border = "3px solid lightcoral";

}

function drop(e) {
    e.preventDefault();
    leftbox.innerHTML = e.dataTransfer.getData('Picture');
}

function endDrag(e) {
    pic = e.target;
    pic.style.visibility = "hidden";

}

window.addEventListener("load", drag, false);