<?php
    $ip = "123.142.55.116";
    for($i = 0; $i <= strlen($ip); $i++) {
        $ip = str_replace($i, ord($i), $ip);
    }
    $ip = str_replace(".", "", $ip);
    $ip = substr($ip, 0, 10);
    $answer = $ip/2;
    $answer = str_replace(".", "", $answer);
    echo $ip . "\n";
    echo $answer . "\n";
?>
