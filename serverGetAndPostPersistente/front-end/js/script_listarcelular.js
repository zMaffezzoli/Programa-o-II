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
            var linha = "<p style='border: 2px solid #169E90; border-radius: 20px;'>" + 
            "ID: " + c.id + "<br>" + 
            "Modelo: " + c.modelo + "<br>" + 
            "Marca: " + c.marca + "<br>" + 
            "Proprietário: "+ c.proprietario.nome + "</p>";
            $("#listagem").append(linha);
        };
    }
    else{
        alert(celular.resultado + " " + celular.detalhes)
    }
});

action.fail(function (){
    alert("Back-end não está disponível :/");
});