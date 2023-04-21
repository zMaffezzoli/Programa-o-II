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
            "<td class='linha_dados'>" + p.id + "</td>" + 
            "<td class='linha_dados'>" + p.nome + "</td>" + 
            "<td class='linha_dados'>" + p.email + "</td>" + 
            "<td class='linha_dados'>" + p.sexo + "</td>" + 
            "<td class='linha_dados'>" + p.data_nascimento + "</td>" + 
            "</tr>";
            $("#dados").append(linha);
        };
    }
    else{
        alert(pessoa.resultado + " " + pessoa.detalhes)
    }
});

action.fail(function (){
    alert("Back-end não está disponível :/");
});
