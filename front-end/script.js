

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
}

function fecharModal(idModal) {
    var modal = document.getElementById(idModal);
    let globo = document.getElementById("globo");
    globo.style.display = "block";
    modal.style.display = "none";
}
