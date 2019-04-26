<?php

require_once __DIR__.'/HER.php';

$array = [
    'christmas' => [
    	'greetings' => [
        	'Merry christmas!',
        	'Spam, PHP, Eggs',
        	'example' => true,
        ]
    ],
    'HER' => [
    	'cool' => true,
    	'useless' => false,
    ],
    'XML' => [
    	'useless',
    	'old_style',
    ],
    'JSON' => [
    	'useless',
    	'old_style',
    ]
];

$encoded = her_encode($array);
echo $encoded.PHP_EOL;


$decoded = her_decode($encoded);
print_r($decoded);


$json = json_encode($decoded, JSON_PRETTY_PRINT);
echo $json.PHP_EOL;