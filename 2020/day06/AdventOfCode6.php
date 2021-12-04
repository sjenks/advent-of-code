<?php

$contents = file_get_contents('input.txt');
$lines = explode("\n", $contents);

$running_total = 0;

$current_answers = [];
$num_people = 0;
foreach($lines as $line) {
	if(empty($line)) {
		foreach($current_answers as $key => $val) {
			if($val === $num_people) {
				$running_total++;
			}
		}
		$current_answers = [];
		$num_people = 0;
	} else {
		$num_people++;
		$letters = str_split($line);
		foreach($letters as $l) {
			if(!array_key_exists($l, $current_answers)) {
				$current_answers[$l] = 1;
			} else {
				$val = $current_answers[$l];
				$val++;
				$current_answers[$l] = $val;
			}
		}
	}
}

echo($running_total . "\n");