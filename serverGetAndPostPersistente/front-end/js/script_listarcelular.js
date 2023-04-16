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
            "<td style='border: 1px solid black; border-collapse: collapse;'>" + c.id + "</td>" + 
            "<td style='border: 1px solid black; border-collapse: collapse;'>" + c.modelo + "</td>" + 
            "<td style='border: 1px solid black; border-collapse: collapse;'>" + c.marca + "</td>" + 
            "<td style='border: 1px solid black; border-collapse: collapse;'>" + c.proprietario.nome + "</td>" + 
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