<?php
require_once 'functions.php';

try {
    $redis = new Redis();
    $redis->connect('127.0.0.1', 6379);
} catch (Exception $e) {
	die($e->getMessage());
}

$scan_file = "";
if (isset($_POST["url"])) {
    $scan = scan($_POST["url"]);
    $scan_file = "tmp/". random_string(16) . ".html";
    file_put_contents($scan_file, substr($scan["result"], 0, 2097152));
}

?>
<!DOCTYPE html>
<html>
<head>
    <!-- Bootstrap core CSS -->
    <link href="/assets/css/bootstrap.min.css" rel="stylesheet">
    <!-- custom CSS -->
    <link href="/assets/css/style.css" rel="stylesheet">

    <title>SSRF Tutorial</title>
    <meta charset="utf-8">
</head>
<body>
    
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top" id="mainNav" style="position: relative; background-color: black !important;">
        <div class="container">
            <a class="navbar-brand js-scroll-trigger" href="">SSRF</a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarResponsive">
                <ul class="navbar-nav ml-auto">
                    <li class="nav-item">
                        <a class="nav-link js-scroll-trigger" href="/">Scanner</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link js-scroll-trigger" href="/admin.php">Admin</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

    <section style="width: 800px; margin-right: auto; margin-left: auto; margin-top: 40px">
        <p style="color: green">
            Ce challenge vise à tester et/ou approfondir vos connaissances sur les
            attaques de type Server Side Request Forgery (SSRF). Cette attaque consiste
            à forcer le serveur (victime) à envoyer une requête vers une ressource
            interne. Cela s'avère problématique pour de nombreuses raisons:
        </p>
        <ul>
            <li style="color: #e8c7c7">
                Certaines applications assument qu'une requête provenant de l'interne a été
                envoyée par un utilisateur fiable et néglierons de se protéger adéquatement
                contre celle-ci.
            </li></br>
            <li style="color: #e8c7c7">
                Un SSRF permet souvent de lire des fichiers sur le serveur de la victime.
            </li></br>
            <li style="color: #e8c7c7">
                Il arrive que ce genre d'attaque permette d'exploiter des applications qui
                roulent à l'interne, ce qui augmente grandement la surface d'attaque et peut
                même mener à du Remote Code Execution (RCE) sur le serveur attaqué.
            </li>
        </ul>
        <p style="color: green">
            Pour plus d'informations, voir
            <a style="text-decoration: underline;" href="https://www.owasp.org/index.php/Server_Side_Request_Forgery">Server Side Request Forgery sur OWASP</a>.
        </p></br>
        <p style="color: green">
            Votre cible est un site web qui offre un service de scan gratuit! Vous pouvez scanner
            n'importe quel url sur le web et le serveur fera la requête et vous retournera le résultat.
            Tentez d'abord d'accéder à la page <a style="text-decoration: underline;" href="/admin.php">admin</a>. Bonne chance!
        </p>
    </section>


    <section class="webdesigntuts-workshop">
        <form action="" method="POST">		    
            <input type="text" name="url" placeholder="https://www.wikipedia.org">		    	
            <button>Scan</button>
        </form>
    </section>

    <section style="width: 800px; margin-right: auto; margin-left: auto; margin-top: 40px; margin-bottom: 40px;">
        <iframe style="width: 100%; height: 500px; background-color: gray;" src="<?= $scan_file; ?>" sandbox></iframe>
    </section>

    <!-- Bootstrap core JavaScript -->
    <script src="/assets/js/jquery.min.js"></script>
    <script src="/assets/js/bootstrap.bundle.min.js"></script>

    <!-- Plugin JavaScript -->
    <script src="/assets/js/jquery.easing.min.js"></script>


</body>
</html>
