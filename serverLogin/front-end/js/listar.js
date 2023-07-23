$(function (){

    login = sessionStorage.getItem("login");

    if (login !== null){

        jwt = sessionStorage.getItem("jwt");

        $.ajax({
            url: "http://localhost:5000/listar/Pessoa",
            dataType: "json",
            headers: {Authorization: 'Bearer ' + jwt},
            success: listar,
            error: function (){
                alert("Erro ao receber dados! Verifique o back-end");
            }
        });

        function listar(retorno){
            if (retorno.resultado == "ok"){
                for (var p of (retorno.detalhes)){
                    var linha = "<tr>" +
                    "<td>" + p.id + "</td>" + 
                    "<td>" + p.login + "</td>" + 
                    "<td>" + p.senha + "</td>" + 
                    "</tr>";

                    $("#dados").append(linha);
                }
            }else{
                alert(retorno.resultado + retorno.detalhes);
            }
        }
    }else{
        alert("Você não está logado, por favor, faça seu login! :)");
        window.location = "form.html";
    }
});