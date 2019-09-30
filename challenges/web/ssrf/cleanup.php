<?php
$path = '/var/www/html/tmp/';
while (true) {
    if ($handle = opendir($path)) {
        while (false !== ($file = readdir($handle))) {
            if ($file != "." && $file != "..") {
                if ((time()-filectime($path.$file)) > 5) {
                    unlink($path.$file);
                }
            }
        }
        closedir($handle);
    }
    sleep(5);
}
?>