function mouse ()
{
    var x = document.getElementById("canvas");
    canvas = x.getContext("2d");

    window.addEventListener("mousemove", icon, false);
}

function icon(e) {
    canvas.clearRect(0,0,600,600);//used to clear out the canvas
    var xPos = e.clientX; //e is position of mouse; e.clientX is x-pos of mouse
    var yPos = e.clientY;
    canvas.fillRect(xPos-50, yPos-50, 100, 100);
} //draws rectangle at position of mouse

window.addEventListener("load", mouse, false);