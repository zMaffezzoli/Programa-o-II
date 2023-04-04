$(document).on("click", "#refresh", function(){
    location.reload()
});

var action = $.ajax({
    url: "http://localhost:5000/listar/Pessoa",
    method: "GET",
    dataType: "json"
});

action.done(function (pessoa){
    if (pessoa.resultado == "ok"){
        for (var p of (pessoa.detalhes)){
            var linha = "ID: " + p.id + " Nome: " + p.nome + " Idade: " + p.idade +  " Data de nascimento: " + p.data + " Cidade: " + p.cidade + "</br>";
            $("#listagem").append(linha);
        };
    }else{
        alert(pessoa.resultado + " " + pessoa.detalhes)
    }
});

action.fail(function (){
    alert("Back-end não está disponível :/");
});