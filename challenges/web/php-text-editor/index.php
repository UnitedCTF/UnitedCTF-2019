<?php

session_start();

include "user.php";

$user = loadUser();

if(isset($_GET["source"])) {
    highlight_file(__FILE__);
    exit();
}

include "header.php";

?>
        <div class="text-center">
            <h2>Create file</h2>
            <form method="POST" action="editor.php">
                <label for="file_name">File name: </label> <input type="text" name="file_name" placeholder="my_file" />
                <input type="submit" name="create" value="Create" class="btn btn-primary" />
            </form><br /><br />
            <h2>Your Files</h2>
            <?php
                if(count($user->files) == 0) {
                    echo "No files!<br />";
                }

                foreach($user->files as $file):
            ?>
            File: <?= $file ?>
            <form method="POST" action="editor.php">
                <input type="hidden" name="file_name" value="<?= $file ?>" />
                <input type="submit" value="Edit" class="btn btn-primary" />
            </form>
            <form method="POST" action="editor.php">
                <input type="hidden" name="file_name" value="<?= $file ?>" />
                <input type="submit" name="delete" value="Delete" class="btn btn-danger" />
            </form>
            <br />
            <?php
                endforeach;
            ?>
            <br /><a href="?source">Source</a>
        </div>
    </body>
</html>