<?php
require_once 'utils.php';

$flag = "FLAG-aac1715ed214f22bc6d335d168792e3a";
$success = false;
$username = "";
$password = "";
$php_output = "";
$sql_output = "";
$db = db();

if (isset($_POST["login"])) {
    $username = isset($_POST["username"]) ? $_POST["username"] : "";
    $password = isset($_POST["password"]) ? $_POST["password"] : "";

    try {
        $sql = "SELECT * FROM users WHERE username = '$username' AND password = '$password'";
        $sql_output = fetchAll($db->query($sql));
        
        if (count($sql_output) >= 1) {
            $php_output = $flag;
            $success = true;
        } else {
            $php_output = "Wrong credentials.";
        }
    } catch (Exception $e) {
        $sql_output = $e->getMessage();
    }
}

$output = array(
    "phpout" => $php_output,
    "sqlout" => print_r($sql_output, true),
    "username" => $username,
    "password" => $password,
    "success" => $success,
);
echo json_encode($output);