$(document).on("click", "#refresh", function(){
    location.reload()
});

var action = $.ajax({
    url: "http://localhost:5000/listar/Celular",
    method: "GET",
    dataType: "json"
});

action.done(function (celular){
    if (celular.resultado == "ok"){
        for (var c of (celular.detalhes)){
            var linha = "<tr>" +
            "<td>" + c.id + "</td>" + 
            "<td>" + c.modelo + "</td>" + 
            "<td>" + c.marca + "</td>" + 
            "<td>" + c.proprietario.nome + "</td>" + 
            "</tr>";
            $("#dados_celulares").append(linha);
        };
    }
    else{
        alert(celular.resultado + " " + celular.detalhes)
    }
});

action.fail(function (){
    alert("Back-end não está disponível :/");
});