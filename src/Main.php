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
                    $this->HER .= self::INDENT.'* '.$f.' = '.$v.PHP_EOL;
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
        $i = 0;
        foreach (explode(PHP_EOL, $this->array) as $value) {
            $value = str_replace(' ', '', $value);

            if (strpos($value, '#') === 0) {
                break 1;
            }

            if (strpos($value, '-') === 0) {
                $value = str_replace('-', '', $value);
                $i = $value;
            } elseif (strpos($value, '*') === 0) {
                $value = str_replace('*', '', $value);
                $value = explode('=', $value, 2);
                $arg[$i][] = [$value[0] => $value[1]];
            }
            unset($value);
        }

        return $arg;
    }
}
