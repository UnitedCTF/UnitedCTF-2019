<?php
session_start();

function get_sources($filename, $from, $to) {
    $handle = fopen($filename, "r");
    $result = "";
    $line_index = 1;
    if ($handle) {
        while (($line = fgets($handle)) !== false) {
            if ($line_index >= $from && $line_index <= $to) {
                $result .= $line;
            }
            $line_index++;
        }
        fclose($handle);
    } else {
        $result = "Error opening file.";
    }
    return $result;
}

function db() {
    $db = new Sqlite3("/database.db");
    if(!$db) {
        die($db->lastErrorMsg());
    }
    return $db;
}

function fetchAll($querySet) {
    $result = array();
    while ($row = $querySet->fetchArray(SQLITE3_ASSOC)) {
        $result[] = $row;
    }
    return $result;
}

set_error_handler(function($errno, $errstr, $errfile, $errline, $errcontext) {
    // error was suppressed with the @-operator
    if (0 === error_reporting()) {
        return false;
    }

    throw new ErrorException($errstr, 0, $errno, $errfile, $errline);
});