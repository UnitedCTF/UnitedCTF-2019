<?php

error_reporting(E_ERROR | E_PARSE);

session_start();

include "database.php";

if(isset($_POST["username"]) && isset($_POST["password"])) {
    $username = $_POST["username"];
    $password = $_POST["password"];
    $result = find_person($username)->fetchArray();

    if($result["password"] === $password) {
        $_SESSION["username"] = $username;
        header("Location: /user.php?username=" . $_SESSION["username"]);
        exit();
    }
}

?>

<html>
    <head>
        <meta charset="utf-8" />
        <title>Login</title>
    </head>
    <body>
        <h1>Family Tree Creator</h1>
        
        <h2>Login</h2>
        
        <form target="" method="POST">
            <label for="username">Username:</label><input type="text" name="username" />
            <label for="password">Password:</label><input type="password" name="password" />
            <input type="submit" />
        </form>
    </body>
</html>