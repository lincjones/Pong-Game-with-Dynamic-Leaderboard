let scores;

function run() {
    async function getScore() {
        let response = await fetch('http://127.0.0.1:5000/scores');
        let data = await response.json()
        return data;
    }
    
    getScore().then(data => {
        scores = data
        console.log(scores)
        document.getElementById("n1n").innerHTML = scores[0][0];
        fPlaceHtml = scores[0][1];
        document.getElementById("n1p").innerHTML = fPlaceHtml;
        document.getElementById("n2n").innerHTML = scores[1][0];
        document.getElementById("n2p").innerHTML = scores[1][1];
        document.getElementById("n3n").innerHTML = scores[2][0];
        document.getElementById("n3p").innerHTML = scores[2][1];
        document.getElementById("n4n").innerHTML = scores[3][0];
        document.getElementById("n4p").innerHTML = scores[3][1];
        document.getElementById("n5n").innerHTML = scores[4][0];
        document.getElementById("n5p").innerHTML = scores[4][1];
    })
    setTimeout(() => {
        console.log("updated");
        run();
    
    }, "100");
    
}

window.onload = function () {
    run();
}

