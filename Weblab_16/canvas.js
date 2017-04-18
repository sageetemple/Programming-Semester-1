function text()
{
    var x = document.getElementById("canvas");
    canvas = x.getContext("2d");

    canvas.shadowOffsetX = 4;
    canvas.shadowOffsetY = 4;
    canvas.shadowColor = "rgba(0, 0, 255, .7)";
    canvas.shadowBlur = 6;

    canvas.font = "bold 36px Tahoma";
    canvas.textAlign = "end";
    canvas.save();
    canvas.fillText("Sage", 300, 100);

    canvas.translate(100, 150);
    canvas.fillText("hello", 300, 100);
    
    canvas.rotate(180 * Math.PI/180); //just insert numbers then it reads in radians
    canvas.fillText("boo", 0,0);

    canvas.restore();
    canvas.scale(1.5, 4);//changes size
    canvas.fillText("scales!", 300, 100);

}

window.addEventListener("load", text, false);