var action = $.ajax({
    url: "http://localhost:5000",
    method: "GET",
    datatype: "json"
});

action.done(function (people){
    for (var p of people){
        var linha = p.nome + p.idade + p.cidade + "</br>";
        $("#listagem").append(linha);
    }
});

action.fail(function (){
    alert("Back-end não está disponível :/");
});