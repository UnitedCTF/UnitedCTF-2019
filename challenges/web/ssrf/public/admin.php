<?php if (false): ?>
<p style="color: green">
    Félictation, voici le deuxième flag: FLAG-1ad0b1f556c689d0dd4301ca757ce9c3
</p>
<p style="color: green">
    Nous avons déterminé qu'un SSRF permettait d'accéder à des pages et de lire
    des fichiers à l'interne! La prochaine étape est d'utiliser la vulnérabilité pour
    trouver des services ouverts sur des ports à l'interne.
</p>
<p style="color: green">
    Notez ce qui arrive lors d'une requête sur un port fermé en envoyant un scan sur
    http://localhost:3000:
</p>
<p style="color: #e8c7c7">
    Failed to connect to localhost port 3000: Connection refused
</p>
<p style="color: green">
    Vous aurez le même résultat pour la majorité des autres ports, puisque ceux-ci également fermés.
    Ce qui nous intéresse, c'est de trouver un port (autre que 80) qui est ouvert. Pour ce faire,
    il vous faudra écrire un script pour tester chacun des ports.
</p>
<p style="color: #e8c7c7">
    Pour faciliter votre recherche, notez que le port recherché est entre 6000 et 6500.
    Le flag est FLAG-md5(port trouvé). Si vous trouvez le port 6123, le flag serait FLAG-4ca82b2a861f70cd15d83085b000dbde
</p>
<?php endif; ?>
<?php
$whitelist = array('127.0.0.1', "::1");
$is_admin = false;
if(!in_array($_SERVER['REMOTE_ADDR'], $whitelist)){
    $is_admin = true;
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
        <?php if ($is_admin): ?>
        <p style="color: green">
            Cette page n'est accessible que par localhost.
        </p>
        <?php else: ?>
        <p style="color: green">
            Bien joué! Voici le premier flag: FLAG-2432a0b57e03c3b365296c9ad898bc2a
        </p>
        <p style="color: green">
            Votre prochain défi consiste non pas à accéder à la page admin.php, mais plutôt
            à lire le code source de celle-ci, se trouvant à /var/www/html/admin.php.
        </p>
        <p style="color: #e8c7c7">
            <b>Indice</b>: Les outils pour faire des requêtes
            supportent généralement bien plus que simplement le protocole HTTP. Si vous
            êtes perdu, vous devriez (re)lire <a style="text-decoration: underline;" href="https://www.owasp.org/index.php/Server_Side_Request_Forgery">Server Side Request Forgery sur OWASP</a>.
        </p>
        <?php endif; ?>
        </p>
    </section>

    <!-- Bootstrap core JavaScript -->
    <script src="/assets/js/jquery.min.js"></script>
    <script src="/assets/js/bootstrap.bundle.min.js"></script>

    <!-- Plugin JavaScript -->
    <script src="/assets/js/jquery.easing.min.js"></script>


</body>
</html>