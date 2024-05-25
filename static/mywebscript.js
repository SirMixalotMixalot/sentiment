let RunSentimentAnalysis = ()=>{
    textToAnalyze = document.getElementById("textToAnalyze").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("system_response").innerHTML = xhttp.responseText;
        }else if(this.readyState == 4 && this.status == 500) {
            document.getElementById("system_response").innerHTML = `<b style="color: red;">There was an error: ${xhttp.responseText}</b>`;
        }
    };
    xhttp.open("GET", "sentimentAnalyzer?textToAnalyze"+"="+textToAnalyze, true);
    xhttp.send();
}
