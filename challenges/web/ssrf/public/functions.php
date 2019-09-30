<?php

ini_set("highlight.comment", "green");
ini_set("highlight.default", "#CC0000");
ini_set("highlight.html", "#000000");
ini_set("highlight.keyword", "black; font-weight: bold");
ini_set("highlight.string", "#0000FF");

function highlight_text($text) {
    $tidy = new tidy;

    $config = array(
        'indent'         => true,
        'output-xhtml'   => true,
        'wrap'           => 200
    );
    $tidy->parseString($text, $config, 'utf8');
    $tidy->cleanRepair();

    $text = $tidy;
    $text = trim($text);
    $text = highlight_string("<?php " . $text, true);  // highlight_string() requires opening PHP tag or otherwise it will not colorize the text
    $text = trim($text);
    $text = preg_replace("|^\\<code\\>\\<span style\\=\"color\\: #[a-fA-F0-9]{0,6}\"\\>|", "", $text, 1);  // remove prefix
    $text = preg_replace("|\\</code\\>\$|", "", $text, 1);  // remove suffix 1
    $text = trim($text);  // remove line breaks
    $text = preg_replace("|\\</span\\>\$|", "", $text, 1);  // remove suffix 2
    $text = trim($text);  // remove line breaks
    $text = preg_replace("|^(\\<span style\\=\"color\\: #[a-fA-F0-9]{0,6}\"\\>)(&lt;\\?php&nbsp;)(.*?)(\\</span\\>)|", "\$1\$3\$4", $text);  // remove custom added "<?php "
    
    return $text;
}

function random_string($length = 10) {
    $characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
    $charactersLength = strlen($characters);
    $randomString = '';
    for ($i = 0; $i < $length; $i++) {
        $randomString .= $characters[rand(0, $charactersLength - 1)];
    }
    return $randomString;
}

function scan($url) {
    $res = "";
    $error = "";

    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_TIMEOUT, 1);
    curl_setopt($ch, CURLOPT_FAILONERROR, true);
    curl_setopt($ch, CURLOPT_WRITEFUNCTION, function ($ch, $recv) use (&$res) {
        $res .= $recv;
        return strlen ( $recv );
    } );
    curl_exec($ch);
    if (curl_error($ch)) {
        $error = curl_error($ch);
    }
    curl_close($ch);

    return array(
        "url" => $url,
        "result" => $error == "" ? $res : $error
    );
}