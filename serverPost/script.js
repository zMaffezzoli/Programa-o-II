$(document).on("click", "#enviar", function(){
    var receber = $("#formulario").serializeArray();

    var chave_valor = {};

    for (var i = 0; i < receber.length; i++) {
        chave_valor[receber[i]['name']] = receber[i]['value'];
    };

    var dados_json = JSON.stringify(chave_valor);

    var action = $.ajax({
        url: "localhost:5000/incluir_pessoas",
        method: "post",
        dataType: "json",
        contentType: "aplication/json",
        data: dados_json
    });

    action.done(function (retorno){
        if (retorno.resultado=="Tudo certo! :)"){
            alert("Deu certo! Você foi incluso");
        }else{
            alert("Não deu certo!" + retorno.detalhes);
        }
    });
    
    action.fail(function (jqXHR, textStatus) {
        mensagem = encontrarErro(jqXHR, textStatus, rota);
        alert("Erro na chamada ajax: " + mensagem);
    });
});