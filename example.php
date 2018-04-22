<?php

require_once __DIR__.'/vendor/autoload.php';

$array = [
    'Category' => [
        'Cool' => true,
    ],
];
$array = json_encode($array);

$HER = new \hearot\HER\Encoder($array);
echo $HER->toHer();
