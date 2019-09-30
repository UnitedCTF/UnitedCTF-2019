<?php

error_reporting(E_ERROR | E_PARSE);

session_start();
include "database.php";

if(!isset($_GET["username"])) {
    exit();
}

$username = $_GET["username"];
$user = find_person($username)->fetchArray();

if($user === false) {
    echo "Invalid user.";
    exit();
}

?>

<html>
    <head>
        <meta charset="utf-8" />
        <title><?php echo htmlspecialchars($username); ?></title>
    </head>
    <body>
        <h1><?php echo htmlspecialchars($username); ?>'s user page</h1>
        First Name: <?php echo htmlspecialchars($user["first_name"]); ?><br />
        Last Name: <?php echo htmlspecialchars($user["last_name"]); ?><br />
        Tree:

        <?php

        if(isset($_SESSION["username"]) && $username === $_SESSION["username"]) {
            $decrypted = decrypt_tree($user["tree"], $user["password"]);

            if(!preg_match("/^[a-z0-9_.\-,|+=\/]+$/i", $decrypted)) {
                echo "An error happened while decrypting your family tree.";
            } else {
                echo $decrypted;
            }
        } else {
            echo $user["tree"] . " (encrypted)";
        }

        ?>
        <br />
    </body>
</html>