<?php

define("UPLOAD_BASE", "uploads/" . session_id() . "/");

if(!file_exists(UPLOAD_BASE)) {
    mkdir(UPLOAD_BASE);
    file_put_contents(UPLOAD_BASE . ".htaccess", "<FilesMatch \"\\.(php|php\\.)\$\">\nOrder Allow,Deny\nDeny from all\n</FilesMatch>");
}

class User {
    function __construct($name, $dev) {
        $this->name = $name;
        $this->dev = $dev;
        $this->files = [];
        $this->do = [];
        $this->undo = [];
    }

    function save() {
        setcookie("profile", base64_encode(serialize($this)));
    }

    function addFile($file_name) {
        $file_path = UPLOAD_BASE . $file_name;

        if(!file_exists($file_path)) {
            touch($file_path);
        } else {
            echo "File already exists.";
            die();
        }

        $this->files[] = $file_name;
        $this->save();
    }

    function renameFile($file_name, $new_name) {
        $file_path = $this->resolve($file_name);
        $new_path = UPLOAD_BASE . $new_name;

        if(file_exists($new_path)) {
            echo "File already exists.";
            die();
        }

        rename($file_path, $new_path);
        
        $index = array_search($file_name, $this->files);
        $this->files[$index] = $new_name;
        $this->save();
    }

    function removeFile($file_name) {
        $file_path = $this->resolve($file_name);
        unlink($file_path);
        $index = array_search($file_name, $this->files);
        array_splice($this->files, $index);
        $this->save();
    }

    function resolve($file_name) {
        if(!in_array($file_name, $this->files)) {
            die();
        }

        return UPLOAD_BASE . $file_name;
    }
}

function loadUser() {
    if(!isset($_COOKIE["profile"])) {
        header("Location: /register.php");
        die();
    }
    
    $user = unserialize(base64_decode($_COOKIE["profile"]));
    
    if(!$user->dev) {
        include "header.php";
        echo '<div class="alert alert-danger">Not a developer! This website is only open to the developers at this time.</div>';
        die();
    }

    return $user;
}