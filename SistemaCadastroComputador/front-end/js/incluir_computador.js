$(document).on("click", "#enviar", function(){
    var receber = $("#formulario").serializeArray();

    var chave_valor = {};

    for (var i = 0; i < receber.length; i++){
        chave_valor[receber[i]['name']] = receber[i]['value'];
    };

    var dados_json = JSON.stringify(chave_valor);

    var action = $.ajax({
        url: "http://localhost:5000/incluir/Computador",
        method: "POST",
        dataType: "json",
        contentType: "application/json",
        data: dados_json
    });

    action.done(function (retorno){
        if (retorno.resultado == "ok"){
            alert("Deu certo! O celular foi incluso");
        }else{
            alert("Não deu certo! Detalhes: " + retorno.detalhes);
        }
    });

    action.fail(function (){
        alert("Erro na chamada ajax!");
    });
});

carregarOption("proprietario_id", "Pessoa");

function carregarOption(selection_id, nome_classe){
    var action = $.ajax({
        url: "http://localhost:5000/listar/" + nome_classe,
        dataType: "json"
    });

    action.done(function (retorno){
        if (retorno.resultado == "ok"){
            incluirOption(selection_id, retorno.detalhes);
        }
    });
};

function incluirOption(selection_id, dados){
    for (var d of dados){
        $("#"+ selection_id).append('<option value="'+d.id+'">'+d.nome+'</option>');
    }
};