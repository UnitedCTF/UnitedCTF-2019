<?php

error_reporting(E_ERROR | E_PARSE);

session_start();

include "database.php";

if(isset($_POST["username"]) && isset($_POST["password"])) {
    $username = $_POST["username"];
    $password = $_POST["password"];
    $first_name = $_POST["first_name"];
    $last_name = $_POST["last_name"];
    $tree = $_POST["tree"];

    if($password === "") {
        echo "Your password must not be empty!";
        die();
    }

    $result = create_person($username, $password, $first_name, $last_name, $tree, "");
    if($result !== true) {
        echo $result;
    } else {
        $_SESSION["username"] = $username;
        header("Location: /user.php?username=" . $_SESSION["username"]);
    }

    exit();
}

?>

<html>
    <head>
        <meta charset="utf-8" />
        <title>Register</title>
    </head>
    <body>
        <h1>Family Tree Creator <?php echo isset($_SESSION["username"]) ? " - " . $_SESSION["username"] : ""; ?></h1>
        
        <?php if(!isset($_SESSION["username"])): ?>

        <h2>Login</h2>
        <h3>Login to view your account</h3>
        <a href="/login.php">Login page</a>
        <?php else: ?>
        <h2><a href="/logout.php">Log out</a></h2>
        <?php endif; ?>

        <h2>Register</h2>
        <h3>Register now to create your family tree</h3>
        
        <form target="" method="POST">
            <label for="username">Username:</label><input type="text" name="username" /><br />
            <label for="password">Password:</label><input type="password" name="password" /><br />
            <label for="first_name">First Name:</label><input type="text" name="first_name" /><br />
            <label for="last_name">Last Name:</label><input type="text" name="last_name" /><br />
            <label for="tree">Family Tree (each generation on a new line, siblings separated by commas): <br /></label>
            <textarea name="tree" placeholder="parent1,parent2&#10;grandparent1,grandparent2"></textarea><br />
            <input type="submit" />
        </form>
    </body>
</html>