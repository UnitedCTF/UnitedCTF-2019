<?php
require_once 'utils.php';

$flag = "FLAG-3510f49d883a12efafc69f8afe3fbc33";
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
        $sql = "SELECT * FROM users WHERE username != 'admin' AND (username = '$username' AND password = '$password')";
        $sql_output = fetchAll($db->query($sql));
        
        if (count($sql_output) >= 1) {
            if ($sql_output[0]["username"] == "admin") {
                $php_output = $flag;
                $success = true;
            } else {
                $php_output = "Successfully logged in, but not as an admin.";
            }
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
?>