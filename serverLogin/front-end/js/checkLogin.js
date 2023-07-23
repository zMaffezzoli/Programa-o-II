$(function() {

    login = sessionStorage.getItem("login");
    var mensagem = "";

    if (login == null){
        mensagem = "Você ainda não fez login! <a href=form.html>Faça agora</a>";
    }else{
        mensagem = `Bem vindo, ${login}`;

        $("#menu").html(`
        
        Menu de opções:
        <a href="index.html">Início</a> | 
        <a href="listar.html">Listar</a> |
        <a href=# id="logout">Logout</a>
        `);
    }

    $("#mensagem").html(mensagem);

    $(document).on("click", "#logout", function() {

        sessionStorage.removeItem("login");
        sessionStorage.removeItem("jwt");

        window.location = "index.html";
    });
});