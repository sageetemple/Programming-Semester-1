function mouse ()
{
    var x = document.getElementById("canvas");
    canvas = x.getContext("2d");

    window.addEventListener("mousemove", icon, false);
}

function icon(e) {
    canvas.clearRect(0,0,1000,1000);//used to clear out the canvas
    var xPos = e.clientX; //e is position of mouse; e.clientX is x-pos of mouse
    var yPos = e.clientY;
    var pic = new Image();
    pic.src="https://www-tc.pbs.org/wnet/nature/files/2015/10/SOUL_OF_THE_ELEPHANT_Image012-e1444839827372.jpg";

    pic.addEventListener("load", function() { canvas.drawImage(pic, xPos-150, yPos-150, 300, 300)}, false);
} //draws rectangle at position of mouse

window.addEventListener("load", mouse, false);