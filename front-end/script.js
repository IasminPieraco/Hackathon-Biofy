

const api = axios.create({
    baseURL: 'http://localhost:3000'
});

function abrirMenu(num) {
    var menu = document.getElementById("menu");
    var preve = document.getElementById("preve");
    var cancel = document.getElementById("cancel");
    var dias = document.getElementById("dias");
    var data = document.getElementById("data");
    menu.style.display = "block";

    preve.addEventListener("click", async function () {
        switch (num) {
            case 1:
                var previsao = "V";
                break;
            case 2:
                var previsao = "UV";
                break;
            case 3:
                var previsao = "A";
                break;
            case 4:
                var previsao = "A";
                break;
        }

        menu.style.display = "none";
        let medicao =  api.get(`previsao${previsao}/`+ num)
            .then(response => {
                return response.data;
            });
        let matriz =  api.get(`/previsoes${previsao}/ `+ num)
            .then(response => {
                return response.data;
            });
        abrirModal(num);
    });

    cancel.addEventListener("click", function () {
        menu.style.display = "none";
    });
}


function abrirModal(num) {
    var modal = document.getElementById("modal" + num);
    var modais = document.getElementsByClassName('modal');
    var globo = document.getElementById("globo");

    for (var i = 0; i < modais.length; i++) {
        if (num - 1 != i) {
            modais[i].style.display = "none";
        }
    }

    if (modal.style.display !== "block") {
        globo.style.display = "none";
        modal.style.display = "block";
    } else {
        globo.style.display = "block";
        modal.style.display = "none";
    }

    const xArray = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15];
    const yArray = [7, 8, 8, 9, 9, 10, 11, 12, 13, 14, 15];
    // Define Data
    const data = [{
        x: xArray,
        y: yArray,
        mode: "lines",
        line: { color: 'blue' }
    }];

    // Define Layout
    const layout = {
        xaxis: { range: [5, 16], title: "Dias", tickfont: { color: 'white' }, titlefont: { color: "white" } },
        yaxis: { range: [0, 20], title: "Previsão", tickfont: { color: 'white' }, titlefont: { color: "white" } },
        title: "",
        titlefont: { color: "white" },
        plot_bgcolor: 'rgba(255,255,255,0.2)', // Define o fundo do gráfico como transparente
        paper_bgcolor: 'rgba(0,0,0,0)',
        legend: { font: { color: 'white' } } // Define a cor da legenda
    };

    
    Plotly.newPlot("ar", data, layout);
    Plotly.newPlot("fogo", data, layout);
    Plotly.newPlot("terra", data, layout);
    Plotly.newPlot("agua", data, layout);
}

function fecharModal(idModal) {
    var modal = document.getElementById(idModal);
    let globo = document.getElementById("globo");
    globo.style.display = "block";
    modal.style.display = "none";
}
