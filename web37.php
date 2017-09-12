<?php
    $fd = fopen('hello.txt', 'w');
    fwrite($fd, 'hello');
    fclose($fd);
    $fd = fopen('hello.txt', 'w');
    fwrite($fd, 'world');
    fclose($fd);
?>
