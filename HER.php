<?php

function her_encode($array)
{
    $HER = '';
    foreach ($array as $arg => $value) {
        if (isset($value)) {
            $HER .= '- '.$arg.' -'.PHP_EOL;
            foreach ($value as $f => $v) {
                $HER .= '  * '.$f.' = '.$v.PHP_EOL;
            }
        } else {
            //$this->HER .= '* '.$arg.PHP_EOL; /* to fix */
        }
    }

    return $HER;
}

function her_decode($HER)
{
    $i = 0;
    $array = [];
    foreach (explode(PHP_EOL, $HER) as $value) {
        $value = str_replace(' ', '', $value);
        if (strpos($value, '#') === 0) {
            continue;
        }

        if (strpos($value, '-') === 0) {
            $value = str_replace('-', '', $value);
            $i = $value;
        } elseif (strpos($value, '*') === 0) {
            $value = str_replace('*', '', $value);
            $value = explode('=', $value, 2);
            $array[$i][] = [$value[0] => $value[1]];
        }
        unset($value);
    }

    return $array;
}
