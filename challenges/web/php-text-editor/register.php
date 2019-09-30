<?php

session_start();

include "user.php";

if(isset($_POST["name"])) {
    $dev = false;
    $user = new User($_POST["name"], $dev);
    $user->save();

    header("Location: /");
    die();
}

include "header.php";

?>
        <div class="text-center">
            <h2>Create your profile</h2>
            <p>
                Please create a profile before accessing the editor.
            </p>
            <form method="POST" action="register.php">
                <label for="name">Name:</label><input type="text" name="name" /><br />
                <input type="submit" class="btn btn-primary"/>
            </form>
        </div>
    </body>
</html>