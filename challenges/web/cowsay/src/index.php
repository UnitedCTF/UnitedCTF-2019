<html>
    <head>
        <title>What does the cow say?</title>
        <link href="https://fonts.googleapis.com/css?family=Lato&display=swap" rel="stylesheet">
        <style>
            * {
                font-family: 'Lato', sans-serif;
                padding: 0px;
                margin: 0px;
            }
            body {
                background-image: url("/images/grass.jpg");
                background-color: rgba(0,0,0,0.5);
            }
            h1 {
                text-align: center;
                padding: 40px;
            }
            .cow {
                display: block;
                margin: auto;
                background-image: url("/images/cow.jpg");
                width: 400px;
                height: 500px;
                -moz-box-shadow: 0px 10px 32px 8px rgba(0,0,0,0.75);
                -webkit-box-shadow: 0px 10px 32px 8px rgba(0,0,0,0.75);
                box-shadow: 0px 10px 32px 8px rgba(0,0,0,0.75);
                overflow-y: auto;
            }
            .container {
                border-left: solid 1px black;
                border-right: solid 1px black;
                width: 800px;
                height: 100%;
                background: white;
                margin: auto;
            }
            form {
                width: 100%;
                padding-top: 40px;
                text-align: center;
            }
            input {
                width: 400px;
            }
            pre {
                font-family: monospace;
            margin: auto;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>What does the cow say?</h1>
            <div class="cow">
<pre>
<?php
if (isset($_GET["say"])) {
    $a = $_GET["say"];
    echo `/usr/games/cowsay $a`;
}
?>
</pre>
            </div>
            <form action="." method="GET">
                <input name="say"/>
                <input type="submit" value="Say it!"/>
            </form>
        </div>
    </body>
</html>
