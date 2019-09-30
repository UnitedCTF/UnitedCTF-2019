<!DOCTYPE HTML>
<?php

  if (isset($_GET['source'])) {
    highlight_file(__FILE__);
    die();
  }


  require('secrets.php');

?>
<html>
  <head>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
  </head>
  <body>
    <div class="container text-center mt-5">
      <h1>The Unhackable Token Generator</h1>
      <hr/>
      <p>This is a demo for our uncrackable token generator service.</p>
      <p>
        It allows users to generate <b>compressed</b> and <b>encrypted</b> tokens containing
        <b>user-specified data</b>.
      </p>
      <p>
        To detect tampering, we added a secret <b>flag</b> after the data.
      </p>
      <p>Click <a target="_blank" href="?source">Here</a> to view how the service works.</p>
    </div>

    <hr>

    <div class="container text-center mt-5">
        <form action="">
          <input name="data" type="text" class="form-control" placeholder="Data to encrypt"/>
          <input type="Submit" class="btn btn-primary mt-2"/>
        </form>
    </div>

    <?php if (isset($_GET['data'])) { ?>

      <hr>

      <div class="container text-center mt-5">
        <?php
          $data = $_GET['data'] . $FLAG;
          $compressed = zlib_encode($data,  ZLIB_ENCODING_GZIP);
          $encrypted = openssl_encrypt($compressed, 'aes-192-cfb', $KEY, 0, 'abcdefghijklmnop');
        ?>
          <h4>Generated token :</h4><b><?php echo $encrypted; ?></b>
      </div>
    <?php } ?>

  </body>
</html>
