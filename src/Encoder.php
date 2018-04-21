<?php

namespace hearot\HER;

class Encoder {
	private $array;
	private $HER = NULL;
	const INDENT = '    ';

	public function __construct($array){
		$this->array = (strpos($array, '{') === 0) ? json_decode($array, true) : $array;
	}

	public function toHER(){
		$this->HER = NULL;
		foreach($this->array as $arg => $value){
			if((isset($value)) and (count($value) > 0)){
				$this->HER .= '- '.$arg.' -'.PHP_EOL;
				foreach($value as $f => $v) $this->HER .= self::INDENT.'* '.$f.' = '.$v.PHP_EOL;
			} else {
				//$this->HER .= '* '.$arg.PHP_EOL; /* to fix */
			}
		}
		return $this->HER;
	}
}
