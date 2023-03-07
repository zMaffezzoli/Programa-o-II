var action = $.ajax({
    url: "http://localhost:5000/listar_pessoas",
    method: "GET",
    datatype: "json"
});

action.done(function (people){
    for (var p of people){
        var linha = "Nome: " + p.nome + " Idade: " + p.idade +  " Data de nascimento: " + p.data + " Cidade: " + p.cidade + "</br>";
        $("#listagem").append(linha);
    }
});

action.fail(function (){
    alert("Back-end não está disponível :/");
});