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
            var linha = "<p style='border: 2px solid #EA9009; border-radius: 20px;'>" + 
            "ID: " + p.id + "<br>" + 
            "Nome: " + p.nome + "<br>" +
            "Idade: " + p.idade + "<br>" +
            "Data de nascimento: " + p.data_nascimento + "<br>" +
            "Cidade: " + p.cidade + "</p>";
            $("#listagem").append(linha);
        };
    }
    else{
        alert(pessoa.resultado + " " + pessoa.detalhes)
    }
});

action.fail(function (){
    alert("Back-end não está disponível :/");
});