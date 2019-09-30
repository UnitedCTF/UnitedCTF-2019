<?php
require_once 'utils.php';

$flag = "FLAG-0783985441fffd91df30f3d4bda79a84";
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
        $sql = "SELECT * FROM users WHERE username = '$username'";
        $sql_output = fetchAll($db->query($sql));
        
        if (count($sql_output) >= 1) {
            if (strtoupper(bin2hex(md5($password, true))) === $sql_output[0]["password"]) {
                $php_output = $flag;
            } else {
                $php_output = "Invalid password.";
            }
        } else {
            $php_output = "Username doesn't exists.";
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
);
echo json_encode($output);
?>
