<?php

session_start();

function checkFileName($file_name) {
    if(strstr($file_name, "..") !== false || strstr($file_name, "/") !== false || strstr($file_name, "\\") !== false) {
        die();
    }
}

include "user.php";

$user = loadUser();

if(!isset($_POST["file_name"])) {
    header("Location: /");
    die();
}

$file_name = $_POST["file_name"];

if(isset($_POST["create"])) {
    checkFileName($file_name);
    $user->addFile($file_name);
}

$file_path = $user->resolve($file_name);

if(isset($_POST["rename"])) {
    $new_file_name = $_POST["new_file_name"];
    checkFileName($new_file_name);
    $user->renameFile($file_name, $new_file_name);

    $file_name = $new_file_name;
    $file_path = $user->resolve($file_name);
}

if(isset($_POST["delete"])) {
    $user->removeFile($file_name);
    header("Location: /");
    die();
}

if(isset($_POST["content"])) {
    $content = $_POST["content"];
    file_put_contents($file_path, $content);
}

include "header.php";
?>

    <div class="row">
        <div class="col-lg-6 offset-lg-3">
            <div class="text-center">
                <?php
                    if(isset($_POST["content"])):
                ?>
                
                <div class="alert alert-success">File saved!</div>
                
                <?php
                    endif;
                ?>

                File: <?= $file_name; ?><br />

                <form method="POST" action="editor.php">
                    <label for="new_name">New name: </label>
                    <input type="text" name="new_file_name" class="" />
                    <input type="hidden" name="file_name" value="<?= $file_name ?>" />
                    <input type="submit" name="rename" value="Rename" class="btn btn-primary" />
                </form><br /><br />

                <form method="POST" action="editor.php">
                    <label for="content">File content:</label><br /><textarea name="content" class="form-control"><?= htmlspecialchars(file_get_contents($file_path)) ?></textarea><br />
                    <input type="hidden" name="file_name" value="<?= $file_name ?>" /><br />
                    <input type="submit" name="save" value="Save" class="form-control btn btn-primary" />
                </form>
                <a href="/" class="page-link">Back</a>
            </div>
        </div>
    </div>
</body>
</html>