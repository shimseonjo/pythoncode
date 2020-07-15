var myWindow;

function openwin(){
    myWindow =window.open("","mywindow","top=100,left=100,width=200,height=100");
    myWindow.document.write("<p>this is mywindow</p>")
}

function closewin(){
    myWindow.close();
}