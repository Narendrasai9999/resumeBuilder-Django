function PrintDiv() {
    let tmp = document.body.innerHTML;
    var divContents = document.getElementById("resume").innerHTML;  
    document.body.innerHTML = divContents;
    window.print();
    document.body.innerHTML=tmp;

}