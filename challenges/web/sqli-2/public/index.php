<?php
ob_start();
    include 'api.php';
    $response = json_decode(ob_get_contents(), true);
ob_end_clean();

$username = $response["username"];
$password = $response["password"];
$sql_output = $response["sqlout"];
$php_output = $response["phpout"];
$php_code = get_sources("api.php", 12, 33);
?>

<!DOCTYPE html>
<html>
<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <link rel="stylesheet" href="assets/css/bootstrap.min.css">
    <link rel="stylesheet" href="assets/css/highlight/default.css">
    <link rel="stylesheet" href="assets/css/highlight/vs2015.css">
    <link rel="stylesheet" href="assets/css/styles.css">

    <title>SQLi-2</title>
</head>
<body>

    <!-- Navigation -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top">
        <div class="container">
            <a class="navbar-brand" href="/">SQLI-2</a>
        </div>
    </nav>

    <main role="main" class="main-container">
        <div class="row">
            <div class="starter-template">
                <h1>SQLI-2</h1>
                <p class="lead">Order of operations</p>
            </div>
        </div>
        <hr>
        <div class="row">
            <div class="col-lg-6">
                <h5>PHP code <a class="btn btn-primary" data-toggle="collapse" href="#phpcode" role="button" aria-expanded="true" aria-controls="phpcode">Toggle</a></h5>
                <pre><code id="phpcode" class="collapse show mycode"><?php echo $php_code; ?></code></pre>

                <h5>SQL command <a class="btn btn-primary" data-toggle="collapse" href="#sqlcode" role="button" aria-expanded="true" aria-controls="sqlcode">Toggle</a></h5>
                <pre><code id="sqlcode" class="collapse show mycode"></code></pre>
                <h5>PHP output <a class="btn btn-primary" data-toggle="collapse" href="#phpout" role="button" aria-expanded="true" aria-controls="phpout">Toggle</a></h5>
                <pre><code id="phpout" class="collapse show mycode json"><?php echo $php_output; ?></code></pre>
                <h5>SQL output <a class="btn btn-primary" data-toggle="collapse" href="#sqlout" role="button" aria-expanded="true" aria-controls="sqlout">Toggle</a></h5>
                <pre><code id="sqlout" class="collapse show mycode json"><?php echo $sql_output; ?></code></pre>
            </div>
            <div class="col-lg-6 login-form">
                <div class="panel row" style="text-align: center">
                    <div class="col">
                        <h5>Login</h5>
                    </div>
                </div>
                <div class="row">
                    <div class="col">
                        <form method="POST" action="">
                            <div class="form-group">
                                <input type="text" class="form-control" placeholder="username" name="username" id="name_input" onkeydown="input_changed()" value="<?php echo $username; ?>" />
                            </div>

                            <div class="form-group">
                                <input type="password" class="form-control" placeholder="password" name="password" id="pwd_input" onkeydown="input_changed()" value="<?php echo $password; ?>" />
                            </div>

                            <button type="submit" class="btn btn-primary" style="width: 100%;" name="login">Login</button>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </main><!-- /.container -->

    <script src="assets/js/jquery-3.3.1.slim.min.js"></script>
    <script src="assets/js/popper.min.js"></script>
    <script src="assets/js/bootstrap.min.js"></script>
    <script src="assets/js/highlight.pack.js"></script>
    <script>hljs.initHighlightingOnLoad();</script>
    <script>
        var interval;
        var phpout     = document.getElementById('phpout');
        var sqlout     = document.getElementById('sqlout');
        var name_input = document.getElementById("name_input");
        var pwd_input  = document.getElementById("pwd_input");
        var sqlcode    = document.getElementById("sqlcode");
        var loading_img = '<img src="assets/img/loading.gif" height=25 width=25 />'
        update_sql();

        function update_sql() {
            sql  = "SELECT * FROM users WHERE username != 'admin' AND (username = '";
            sql += name_input.value;
            sql += "' AND password = '";
            sql += pwd_input.value;
            sql += "')";

            sqlcode.textContent = sql;
            hljs.initHighlighting.called = false;
            hljs.initHighlighting();
        }

        function input_changed() {
            setTimeout(() => {
                clearTimeout(interval);
                update_sql();
                phpout.innerHTML = loading_img;
                sqlout.innerHTML = loading_img;

                interval = setTimeout(function() {
                    var http = new XMLHttpRequest();
                    var url = 'api.php';
                    params = 'username=' + name_input.value;
                    params += "&password=" + pwd_input.value;
                    params += "&login=1";

                    http.open('POST', url, true);

                    //Send the proper header information along with the request
                    http.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
                    http.onreadystatechange = function() {
                        if (http.readyState == 4 && http.status == 200) {
                            var response = JSON.parse(this.responseText);
                            phpout.innerHTML = response.phpout;
                            sqlout.innerHTML = response.sqlout;
                            hljs.initHighlighting.called = false;
                            hljs.initHighlighting();
                        }
                    }
                    http.send(params);
                }, 1000);
            }, 50);
        }
    </script>
</body>
</html>