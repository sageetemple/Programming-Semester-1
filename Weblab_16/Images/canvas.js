function text()
{
    var x = document.getElementById("canvas");
    canvas = x.getContext("2d");

   var pic = new Image();
    pic.src="https://www-tc.pbs.org/wnet/nature/files/2015/10/SOUL_OF_THE_ELEPHANT_Image012-e1444839827372.jpg";

    pic.addEventListener("load", function() { canvas.drawImage(pic, 0, 0, x.width, x.height)}, false);

}

window.addEventListener("load", text, false);