$(function (){

    $(document).on("click", "#btLogin", function() {

        var login = $("#login").val();
        var senha = $("#senha").val();

        var dados = JSON.stringify({login: login, senha: senha});

        $.ajax({
            url: "http://localhost:5000/login",
            method: "POST",
            dataType: "json",
            contentType: "application/json",
            data: dados,
            success: loginOk,
            error: function (xhr, status, error){
                alert("Erro na conexão, verifique o backend. " + xhr.responseText + " - " + status + " - " + error);
            }
        });

        function loginOk(retorno){
            if (retorno.resultado == "ok"){
                
                sessionStorage.setItem("login", login);
                sessionStorage.setItem("jwt", retorno.detalhes);
    
                window.location = "index.html";
            }else{
                alert(retorno.resultado + retorno.detalhes);
            }
        }
    });
});