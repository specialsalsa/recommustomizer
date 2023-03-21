let slider = document.getElementById("valence");

let valence = 0.5;

slider.oninput = function() {
    valence = this.value / 100
    console.log(valence)
}

document.getElementById('getRecs').addEventListener('click', async () => {
    const res = await fetch("http://127.0.0.1:5000/getParamsFromBrowser", {
        method: 'POST',
        mode: "cors",
        body: JSON.stringify({"target_valence": valence})
    });

    const data = await res.json();

    console.log(data);
    // console.log("I was pressed");

})