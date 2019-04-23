<?php

require_once __DIR__.'/HER.php';

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

$encoded = her_encode($array);
echo $encoded.PHP_EOL;

$decoded = her_decode($encoded);
print_r($decoded);

$json = json_encode($decoded);
echo $json;
