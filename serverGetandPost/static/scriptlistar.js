$(document).on("click", "#refresh", function(){
    location.reload()
});

var action = $.ajax({
    url: "http://localhost:5000/dados_enviar",
    method: "GET",
    dataType: "json"
});

action.done(function (pessoa){
    for (var p of (pessoa)){
        var linha = "Nome: " + p.nome + " Idade: " + p.idade +  " Data de nascimento: " + p.data + " Cidade: " + p.cidade + "</br>";
        $("#listagem").append(linha);
    }
});

action.fail(function (){
    alert("Back-end não está disponível :/");
});