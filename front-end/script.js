

function abrirModal(num) {
    var modal = document.getElementById("modal" + num);
    var modais = document.getElementsByClassName('modal');
    var globo = document.getElementById("globo");

    for (var i = 0; i < modais.length; i++) {
        if(num -1 != i){
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

    const xArray = [50,60,70,80,90,100,110,120,130,140,150];
        const yArray = [7,8,8,9,9,9,10,11,14,14,15];
        
        // Define Data
        const data = [{
          x: xArray,
          y: yArray,
          mode:"lines",
          line:{color:'blue'}
        }];
        
        // Define Layout
        const layout = {
          xaxis: {range: [40, 160], title: "Dias", tickfont: {color: 'white'}, titlefont:{color:"white"}},
          yaxis: {range: [0, 20], title: "Price in Millions", tickfont: {color: 'white'}, titlefont:{color:"white"}},  
          title: "",
          titlefont:{color:"white"},
          plot_bgcolor: 'rgba(255,255,255,0.2)', // Define o fundo do gráfico como transparente
         paper_bgcolor: 'rgba(0,0,0,0)',
         legend: {font: {color: 'white'}} // Define a cor da legenda
        };
        
        // Display using Plotly
        switch(num){
            case 1:
                Plotly.newPlot("ar", data, layout);
                break;
            case 2:
                Plotly.newPlot("fogo", data, layout);
                break;
            case 3:
                Plotly.newPlot("terra", data, layout);
                break;
            case 4:
                Plotly.newPlot("agua", data, layout);
                break;
        }
}

function fecharModal(idModal) {
    var modal = document.getElementById(idModal);
    let globo = document.getElementById("globo");
    globo.style.display = "block";
    modal.style.display = "none";
}
