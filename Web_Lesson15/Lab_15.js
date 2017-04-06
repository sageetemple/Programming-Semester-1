/**
 * Created by templetons0379 on 4/5/2017.
 */
function custom() {
    var x = document.getElementById("canvas");
    var g = canvas.createLinearGradient(150, 150, 600, 560);
    g.addColorStop(0, "purple");
    g.addColorStop(.3, "blue");
    g.addColorStop(1, "yellow");

    canvas = x.getContext("2d");
    canvas.strokeStyle="red";
    canvas.fillStyle=g;
    canvas.beginPath();
    canvas.moveTo(150, 150);
    canvas.lineTo(300, 200);
    canvas.lineTo(350, 50);
    canvas.lineTo(400, 200);
    canvas.lineTo(550, 150);
    canvas.lineTo(450, 250);
    canvas.lineTo(600, 280);
    canvas.lineTo(460, 340);
    canvas.lineTo(575, 425);
    canvas.lineTo(400, 410);
    canvas.lineTo(350, 560);
    canvas.lineTo(300, 410);
    canvas.lineTo(125, 425);
    canvas.lineTo(265, 340);
    canvas.lineTo(125, 280);
    canvas.lineTo(275, 255);
    canvas.closePath();
    canvas.stroke();
    canvas.fill();
}

window.addEventListener("load", custom, false);