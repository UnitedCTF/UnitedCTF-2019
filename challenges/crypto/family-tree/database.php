<?php

error_reporting(E_ERROR | E_PARSE);

include "crypto.php";

$db = new SQLite3("family.db");

$sql =<<<EOF
CREATE TABLE IF NOT EXISTS user
(
    username VARCHAR(16) NOT NULL,
    password VARCHAR(255) NOT NULL,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    tree TEXT NOT NULL
);
EOF;

$db->exec($sql);

function find_person($username) {
    global $db;

    $cmd = $db->prepare("SELECT * FROM user WHERE username = :username");
    $cmd->bindValue(":username", $username, SQLITE3_TEXT);
    return $cmd->execute();
}

function create_person($username, $password, $first_name, $last_name, $tree, $flag) {
    global $db;

    if(strlen($username) > 16 || !preg_match("/^[a-z0-9_.\-]+$/i", $username)) {
        return "Bad username";
    }

    $result = find_person($username)->fetchArray();

    if($result !== false) {
        return "Username already exists";
    }

    // Make sure the tree is valid, then encrypt it with the user's password as nonce
    $tree_text = "";

    if($tree !== "") {
        $lines = explode("\n", $tree);

        foreach($lines as $line) {
            if($tree_text !== "") {
                $tree_text .= "|";
            }

            $parents = explode(",", $line);

            foreach($parents as $parent) {
                $result = find_person($parent)->fetchArray();

                if($result === false) {
                    return "Invalid parent";
                }
            }

            $tree_text .= $line;
        }
    }

    $tree_text .= "|" . base64_encode($flag);
    $tree_text = encrypt_tree($tree_text, $result["password"]);

    $cmd = $db->prepare("INSERT INTO user (username, `password`, first_name, last_name, tree) VALUES (:username, :password, :first_name, :last_name, :tree)");
    $cmd->bindValue(":username", $username, SQLITE3_TEXT);
    $cmd->bindValue(":password", $password, SQLITE3_TEXT);
    $cmd->bindValue(":first_name", $first_name, SQLITE3_TEXT);
    $cmd->bindValue(":last_name", $last_name, SQLITE3_TEXT);
    $cmd->bindValue(":tree", $tree_text, SQLITE3_TEXT);
    $result = $cmd->execute();

    return true;
}

// Passwords and $flag from config.php
create_person("eukaryotes", $eukaryotes_password, "Eukaryotes", "", "", "");
create_person("lucy", $lucy_password, "Lucy", "???", "eukaryotes", $flag);

?>