

<<__EntryPoint>>
function main(): void {
	$contents = file_get_contents('input.txt');
	$lines = explode("\n", $contents);
	$nums = [];
	foreach($lines as $line) {
		$nums[] = (int)$line;
	}

	foreach($nums as $i) {
		foreach($nums as $j) {
			$target = 2020 - $i - $j;
			if(in_array($target, $nums)) {
				echo('found ' . $i . ' ' . $j . ' ' . $target . "\n");
				echo($i * $j * $target . "\n");
				return;
			}
		}
	}
}