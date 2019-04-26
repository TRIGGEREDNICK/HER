<?php

function her_formatter($value){
	if($value == '1') return 'True';
	elseif($value == '0') return 'False';
	else return '"'.$value.'"';
}

function array_formatter($value){
	if($value == 'True') return true;
	elseif($value == 'False') return false;
	else return substr($value, 1, -1);
}

function her_encode($array){
	$HER = '';
	$ind = '    ';

	foreach($array as $dictionary => $array_dict){
		$dictionary = ucfirst($dictionary);

		$HER .= '- '.$dictionary.' -'.PHP_EOL;

		$i = 0;
		foreach($array_dict as $arg => $value){

			if(is_array($value)){
				$HER .= $ind.'>> '.ucfirst($arg).'[]'.PHP_EOL;
				$arg = ucfirst($arg);
				foreach($value as $v){
					$v = her_formatter($v);
					$HER .= $ind.'* '.$arg.'[] = '.$v.PHP_EOL;
				}
			} elseif(is_numeric($arg)){
				if($i == 0) $HER .= $ind.'>> Array[]'.PHP_EOL;
				$value = her_formatter($value);
				$HER .= $ind.'* Array[] = '.$value.PHP_EOL;
				$i++;
			} else {
				$value = her_formatter($value);
				$HER .= $ind.' * '.$arg.' = '.$value.PHP_EOL;
			}
		}
	}

	return $HER;
}

function her_decode($HER){
	$r = 0;
	$array = [];
	$ind = '    ';
	$HER = explode(PHP_EOL, $HER);


	foreach($HER as $line){
		//$line = str_replace($ind, '', $line);

		if(stripos($line, '#') === 0) continue;
		elseif(stripos($line, '>>') === 0) continue;
		elseif(stripos($line, '-') === 0){
			$line = substr($line, 2, -2);
			$line = strtolower($line);
			$r = $line;
		} elseif(stripos($line, '*') !== false){
			$value = explode('=', $line, 2);

			$value[0] = str_replace([' ', '*'], '', $value[0]);
			$value[0] = strtolower($value[0]);
			$value[1] = substr($value[1], 1);
			$value[1] = array_formatter($value[1]);

			if(stripos($value[0], '[]') !== false){
				$value[0] = str_replace('[]', '', $value[0]);
				if($value[0] == 'array'){
					$array[$r][] = $value[1];
				} else {
					if(!is_numeric($value[0])) $array[$r][$value[0]][] = $value[1];
					else $array[$r][] = $value[1];
				}
			} else {
				$array[$r][$value[0]] = $value[1];
			}
		}
	}

	return $array;
}
