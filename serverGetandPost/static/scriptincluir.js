var action = $.ajax({
    url: "http://localhost:5000/dados",
    method: "GET",
    dataType: "json"
});

action.done(function (pessoa){
    var linha = "Nome: " + pessoa.nome + " Idade: " + pessoa.idade +  " Data de nascimento: " + pessoa.data + " Cidade: " + pessoa.cidade + "</br>";
    $("#listagem").append(linha);
});

action.fail(function (){
    alert("Back-end não está disponível :/");
});