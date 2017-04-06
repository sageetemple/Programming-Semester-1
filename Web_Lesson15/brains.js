/**
 * Created by templetons0379 on 4/5/2017.
 */
function shapes()
{
    var x = document.getElementById("canvas");
    canvas = x.getContext("2d");
    canvas.strokeStyle = "yellow";
    canvas.fillStyle = "purple";
    canvas.beginPath();
    canvas.moveTo(50, 50);//where the start is
    canvas.lineTo(70, 250);//drawing the line from start to this point
    canvas.lineTo(300, 200);
    canvas.closePath();//meets all the lines
    canvas.stroke();
    canvas.fill();

    //gradient rectangle
    //var g = canvas.createLinearGradient(10, 10, 100, 200);
    //g.addColorStop(0, "blue");
    //g.addColorStop(.2, "green");
    //g.addColorStop(1,"red");
    //canvas.fillStyle = g;

    //this makes the rectangle
    //canvas.fillRect(10, 10, 100, 200);

    //boring colored rectangle
    //canvas.fillStyle= "blue";
    //canvas.strokeStyle= "red";
    //canvas.strokeRect(10, 10, 100, 200);
    //canvas.clearRect(35, 60, 50, 100);

}

window.addEventListener("load", shapes, false);
