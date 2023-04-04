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
            var linha = "ID: " + c.id + " Modelo: " + c.modelo + " Marca: " + c.marca +  " Proprietário: " + c.proprietario.nome + "</br>";
            $("#listagem").append(linha);
        };
    }else{
        alert(celular.resultado + " " + celular.detalhes)
    }
});

action.fail(function (){
    alert("Back-end não está disponível :/");
});