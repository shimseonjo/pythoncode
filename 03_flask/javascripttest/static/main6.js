function func(){
    var season = prompt("좋아하는 계절?","봄");
    var message = "";
    var img ="";

    switch(season){
        case "봄":
            message="봄을 좋아하시네요";
            img="img01.jpg";
            break;
        case "여름":
            message="여름을 좋아하시네요";
            img="img02.jpg";
            break;
        case "가을":
            message="가을을 좋아하시네요";
            img="img03.jpg";
            break;
        case "겨울":
            message="겨울을 좋아하시네요";
            img="img04.jpg";
            break;
        default:
            alert("잘못 입력하셨습니다.");
    }

    document.getElementById('message').innerHTML=message;
    document.getElementById('img').src="/static/img/"+img
}