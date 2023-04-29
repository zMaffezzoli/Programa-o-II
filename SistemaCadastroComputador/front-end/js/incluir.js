function incluir(classe){
    
    $(document).on("click", "#enviar", function(){
        var receber = $("#formulario").serializeArray();
    
        var chave_valor = {};
    
        for (var i = 0; i < receber.length; i++){
            chave_valor[receber[i]['name']] = receber[i]['value'];
        };
    
        var dados_json = JSON.stringify(chave_valor);
    
        var action = $.ajax({
            url: "http://"+ip+":5000/incluir/" + classe,
            method: "POST",
            dataType: "json",
            contentType: "application/json",
            data: dados_json
        });
    
        action.done(function (retorno){
            if (retorno.resultado == "ok"){
                alert("Deu certo! Você foi incluso");
            }else{
                alert("Não deu certo! Detalhes: " + retorno.detalhes);
            }
        });
    
        action.fail(function (){
            alert("Erro na chamada ajax!");
        });
    });
}