<?php

error_reporting(E_ERROR | E_PARSE);

session_start();
session_destroy();

header("Location: /");
exit();

?>