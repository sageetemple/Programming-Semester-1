function validate() {
    var x = document.forms.input.username.value;
    var atPos = x.indexOf("@");
    var dotPos = x.lastIndexOf(".");
    //need....username@webaddress.extension
    //if, the following...
    //need an @...if @ is not in the string
    //@ is in the wrong place
    //there is an extension with final dot in right place
    if (atPos < 1 || dotPos < atPos + 2 || dotPos + 2 > x.length)
        alert("This is not a valid email address.");

    else
        alert("Success!");
}
function passWord() {
    var y = document.forms.input.password.value;
    var l=y.length;
    if( l < 6)
        alert("Your password does not meet the minimum requirements");
    else
        alert("Success!");
}

function both() {
    var x = document.forms.input.username.value;
    var atPos = x.indexOf("@");
    var dotPos = x.lastIndexOf(".");

    var y = document.forms.input.password.value;
    var l = y.length;

    if((atPos < 1|| dotPos< atPos+2|| dotPos + 2 > x.length) && ( l < 6) )
        alert("Both your username and password are incorrect.");
    else {
        if(atPos < 1|| dotPos< atPos+2|| dotPos + 2 > x.length)
            alert("This is not a valid email address.");
        else if( l < 6)
            alert("Your password does not meet the minimum requirements");
        else
            alert("Success!");
        }
    }