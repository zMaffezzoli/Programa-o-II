$(document).on("click", "#refresh", function(){
    location.reload()
});

var action = $.ajax({
    url: "http://localhost:5000/listar/Computador",
    method: "GET",
    dataType: "json"
});

action.done(function (computador){
    if (computador.resultado == "ok"){
        for (var c of (computador.detalhes)){
            var linha = "<tr>" +
            "<td>" + c.id + "</td>" + 
            "<td>" + c.placa_mae + "</td>" + 
            "<td>" + c.processador + "</td>" + 
            "<td>" + c.placa_video + "</td>" + 
            "<td>" + c.memoria_ram + "</td>" + 
            "<td>" + c.fonte + "</td>" + 
            "<td>" + c.proprietario.nome + "</td>" + 
            "</tr>";
            $("#dados").append(linha);
        };
    }
    else{
        alert(computador.resultado + " " + computador.detalhes)
    }
});

action.fail(function (){
    alert("Back-end não está disponível :/");
});