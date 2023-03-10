$(document).on("click", "#enviar", function(){
    var receber = $("#formulario").serializeArray();

    var chave_valor = {};

    for (var i = 0; i < receber.length; i++) {
        chave_valor[receber[i]['name']] = receber[i]['value'];
    };

    var dados_json = JSON.stringify(chave_valor);

    var action = $.ajax({
        url: "http://localhost:5000/dados",
        method: "POST",
        dataType: "json",
        contentType: "application/json",
        data: dados_json
    });

    action.done(function (retorno){
        if (retorno.resultado == "Erro!"){
            alert("Não deu certo! Detalhes: " + retorno.detalhes);
        }else{
            alert("Você foi incluso!");
        }
    });

    action.fail(function (retorno2) {
        alert("Erro na chamada ajax!" + " Detalhes: " + retorno2.detalhes);
    });
});