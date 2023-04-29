function carregarOption(selection_id, nome_classe){
    var action = $.ajax({
        url: "http://"+ip+":5000/listar/" + nome_classe,
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