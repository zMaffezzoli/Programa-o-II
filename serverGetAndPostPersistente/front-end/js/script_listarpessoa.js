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
            "<td style='border: 1px solid black; border-collapse: collapse;'>" + p.id + "</td>" + 
            "<td style='border: 1px solid black; border-collapse: collapse;'>" + p.nome + "</td>" + 
            "<td style='border: 1px solid black; border-collapse: collapse;'>" + p.idade + "</td>" + 
            "<td style='border: 1px solid black; border-collapse: collapse;'>" + p.data_nascimento + "</td>" + 
            "<td style='border: 1px solid black; border-collapse: collapse;'>" + p.cidade + "</td>" + 
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