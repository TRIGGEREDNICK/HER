<?php

require_once __DIR__.'/vendor/autoload.php';

$array = [
    'Category' => [
        'Cool' => 1,
        'ok'   => 1,
    ],
    'Two' => [
        'cool' => 0,
        'ok'   => 0,
    ],
];

$HER = new \hearot\HER\Main($array);
$encoded = $HER->toHer();

echo $encoded.PHP_EOL;
unset($HER);

$HER = new \hearot\HER\Main($encoded);
print_r($HER->toArray());
echo PHP_EOL.$HER->toJSON();
