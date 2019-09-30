<?php

function get_client_ip() {
    $ipaddress = $_SERVER['HTTP_X_FORWARDED_FOR'];
    return explode(",", $ipaddress)[0];
}

$ip = get_client_ip();
$db = new Sqlite3("/web/database.db");
if(!$db) {
    die($db->lastErrorMsg());
}

$msg = "";
$sql = "
    SELECT COUNT(*) tries, timestamp
    FROM access_logs
    WHERE ip = '$ip' AND timestamp > datetime('now', '-1 minutes')
    GROUP BY ip ORDER BY timestamp DESC
";
$result = $db->query($sql)->fetchArray(SQLITE3_ASSOC);

$tries = 0;
if ($result) {
    $tries = $result["tries"];
    $timestamp = new DateTime($result["timestamp"]);
}

if ($tries < 3 && isset($_POST["username"])) {
    $username = isset($_POST["username"]) ? $_POST["username"] : "";
    $password = sha1(isset($_POST["password"]) ? $_POST["password"] : "");

    try {
        $sql = "SELECT * FROM users WHERE username = ':username' AND password = ':password'";
        $stm = $db->prepare($sql);
        $stm->bindValue(":username", $username);
        $stm->bindValue(":password", $password);
        $logged_in = $stm->execute()->fetchArray(SQLITE3_ASSOC);
        
        if ($logged_in) {
            die("You found a bug. Please contact the challenge maker!");
        } else {
            $sql = "INSERT INTO access_logs (ip) VALUES ('$ip')";
            $db->exec($sql);
            $tries++;
            $msg = "Invalid username/password.";
            $timestamp = new DateTime('now');
        }
    } catch (Exception $e) {
        die($e->getMessage());
    }
}


if ($tries >= 3) {
    $now = new DateTime('now');
    $remaining = 60 - $now->diff($timestamp)->s;
    $msg = "Too many failed attempts. Your IP address ($ip) is banned for <span id='time'>$remaining</span> seconds.";
}
?>
<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" href="assets/css/bootstrap.min.css" id="bootstrap-css">
        <link rel="stylesheet" href="assets/css/my.css">
        <script src="assets/js/bootstrap.min.js"></script>
        <script src="assets/js/jquery.min.js"></script>
    </head>
    <body>
        <?php if ($msg != ""): ?>
            <div class="alert alert-danger" id="msg-box" style="position: absolute; width: 40%; left: 30%; top: 7%; text-align: center;">
                <strong><?= $msg ?></strong>
            </div>
        <?php endif; ?>
        <div class="wrapper fadeInDown">
        <div id="formContent">
            <!-- Tabs Titles -->

            <!-- Icon -->
            <div class="fadeIn first">
            <img src="assets/images/lock.png" id="icon" alt="User Icon" />
            </div>

            <!-- Login Form -->
            <form method="POST" action="">
                <input type="text" id="login" class="fadeIn second" name="username" placeholder="login">
                <input type="password" id="password" class="fadeIn third" name="password" placeholder="password">
                <input type="submit" class="fadeIn fourth" value="Log In">
            </form>

            <!-- Remind Passowrd -->
            <div id="formFooter">
                <a class="underlineHover" onclick="alert('sucks to be you');">Forgot Password?</a>
            </div>

        </div>
        </div>
        <script>
            var time = document.getElementById('time');
            if (time) {
                var x = setInterval(() => {
                    var time_span = document.getElementById('time');
                    var time = parseInt(time_span.innerHTML)-1;
                    if (time <= 0) {
                        clearInterval(x);
                        document.getElementById('msg-box').style.display = "none";
                    } else {
                        time_span.innerHTML = time.toString();
                    }
                }, 1000);
            }
        </script>
    </body>
</html>