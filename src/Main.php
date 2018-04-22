<?php

namespace hearot\HER;

class Main
{
    private $array;
    private $HER = null;
    const INDENT = '    ';

    public function __construct($array)
    {
        $this->array = $array;
    }

    public function toHER()
    {
        $this->HER = null;
        foreach ($this->array as $arg => $value) {
            if (isset($value)) {
                $this->HER .= '- '.$arg.' -'.PHP_EOL;
                foreach ($value as $f => $v) {
                    if (strpos($f, '#') === 0) {
                        break 1;
                    } else {
                        $this->HER .= self::INDENT.'* '.$f.' = '.$v.PHP_EOL;
                    }
                }
            } else {
                //$this->HER .= '* '.$arg.PHP_EOL; /* to fix */
            }
        }

        return $this->HER;
    }

    public function toJSON()
    {
        $array = $this->toArray();

        return json_encode($array);
    }

    public function toArray()
    {
    }
}
