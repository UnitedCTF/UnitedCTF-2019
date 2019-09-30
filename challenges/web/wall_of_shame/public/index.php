<?php
session_start();

if (!isset($_GET["page"])) {
    header('Location: /?page=home');
    exit();
}

if (!isset($_SESSION["folder"])) {
    $folder = "/uploads/" . md5(mt_rand()) . "/";
    mkdir(__DIR__ . $folder);
    $_SESSION["folder"] = $folder;
    $_SESSION["files"] = array();
}

if (isset($_FILES["picture"]))
{
    $is_valid = false;
    $error = "";

    if (!file_exists($_FILES["picture"]["tmp_name"])
     || !is_uploaded_file($_FILES["picture"]["tmp_name"])) {
        $error = "You need to upload a file.";
    } else {
        $filename = md5(mt_rand());
        $target_file = __DIR__ . $_SESSION["folder"] . $filename;

        $extension = "";
        $type = exif_imagetype($_FILES["picture"]["tmp_name"]);
        if ($type === IMAGETYPE_GIF)
            $extension = ".gif";
        else if ($type === IMAGETYPE_JPEG)
            $extension = ".jpg";
        else if ($type === IMAGETYPE_PNG)
            $extension = ".png";
        else
            $error = "Only png, jpg or gif are allowed.";
        $target_file .= $extension;

        if ($_FILES["picture"]["size"] > 2000000) {
            $error = "Your file is over 2 MB.";
        }

        if ($error === "") {
            if (!move_uploaded_file($_FILES["picture"]["tmp_name"], $target_file)) {
                $error = "An error happened when uploading your file.";
            } else {
                $_SESSION["files"][] = $filename . $extension;
                header('Location: /?page=wallofshame');
                exit();
            }
        }
    }
}

$page = $_GET["page"] . ".php";
?>

<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <title>Can U Hack!?</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <link rel="stylesheet" href="/assets/css/bootstrap/bootstrap.css" media="screen">
        <link rel="stylesheet" href="/assets/css/slate.min.css">
        <link rel="stylesheet" href="/assets/css/style.css">
        <script src="/assets/js/jquery/jquery.min.js"></script>
        <script src="/assets/js/bootstrap/popper.min.js"></script>
        <script src="/assets/js/freewall/freewall.js"></script>
    </head>
    <body>
        <div class="navbar navbar-expand-lg navbar-dark bg-primary">
            <div class="container">
                <a href="/?page=home" class="navbar-brand">Hack me if you can</a>
                <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarResponsive">
                    <ul class="navbar-nav">
                        <li class="nav-item">
                            <a class="nav-link" href="/?page=home">Home</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="/?page=wallofshame">Wall of Shame</a>
                        </li>
                    </ul>
                </div>
            </div>
        </div>


        <div class="container" id="main">
            <?php include $page; ?>
        </div>

        <script src="/assets/js/bootstrap/bootstrap.min.js"></script>
    </body>
</html>
