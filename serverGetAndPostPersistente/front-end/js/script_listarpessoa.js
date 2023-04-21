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
            var linha = "<tr>" +
            "<td>" + p.id + "</td>" + 
            "<td>" + p.nome + "</td>" + 
            "<td>" + p.idade + "</td>" + 
            "<td>" + p.data_nascimento + "</td>" + 
            "<td>" + p.cidade + "</td>" + 
            "</tr>";
            $("#dados_pessoas").append(linha);
        };
    }
    else{
        alert(pessoa.resultado + " " + pessoa.detalhes)
    }
});

action.fail(function (){
    alert("Back-end não está disponível :/");
});