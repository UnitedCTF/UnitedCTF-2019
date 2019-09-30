<?php

error_reporting(E_ERROR | E_PARSE);

include "config.php";

function encrypt_tree($tree, $nonce) {
    // $key from config.php
    global $key;

    $encrypted = openssl_encrypt($tree, "aes-256-ctr", $key, OPENSSL_RAW_DATA, $nonce);
    return base64_encode($encrypted);
}

function decrypt_tree($encrypted, $nonce) {
    // $key from config.php
    global $key;

    return openssl_decrypt(base64_decode($encrypted), "aes-256-ctr", $key, OPENSSL_RAW_DATA, $nonce);
}

?>