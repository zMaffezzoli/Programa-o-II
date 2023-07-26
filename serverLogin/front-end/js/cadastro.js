$(function (){

    let login = sessionStorage.getItem("login");

    if(login !== null){
        alert("Você já está logado!");
        window.location = "index.html";
    };
});

function cadastro(classe){
    $(document).on("click", "#btCadastro", function() {
        var login = $("#login").val();
        var senha = $("#senha").val();

        var dados = JSON.stringify({login: login, senha: senha});

        $.ajax({
            url: "http://localhost:5000/cadastro/" + classe,
            method: "POST",
            dataType: "json",
            contentType: "application/json",
            data: dados,
            success: cadastroOk,
            error: function (xhr, status, error){
                alert("Erro na conexão, verifique o backend. " + xhr.responseText + " - " + status + " - " + error);
            }
        });

        function cadastroOk(retorno){
            if (retorno.resultado == "ok"){
                alert("Você foi cadastrado!");
                window.location = "form.html";
            }else{
                alert(retorno.resultado + retorno.detalhes)
            }
        }
    });
};