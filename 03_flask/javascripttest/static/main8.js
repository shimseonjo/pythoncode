
function gugu(){
    var dan = document.getElementById("dan").value;
    var str="";
    for(var i=1;i<=9;i++){
        str+= dan + " X " + i + " = " + dan*i +"<br>";
    }
    document.getElementById("result").innerHTML=str;
}

function enter(){
    console.log(window.event.keyCode);
    if(window.event.keyCode==13){
        gugu();
    }
}

