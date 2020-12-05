<?hh
// @format

final class AdventOfCodeDay2 extends ScriptController {
  <<__Override>>
  protected async function genRun(): Awaitable<int> {
    $file = Filesystem::readFile('/data/users/sjenks/www/flib/intern/scripts/analytics/scott/day2/input.txt');
    $split = Str\split($file, "\n");

    $valid_passwords = 0;
    foreach($split as $f) {
      $line_bits = Str\split($f, ' ');
      if(PHP\count($line_bits) < 2) {
        continue;
      }
      $range = $line_bits[0];
      $valid_letter = $line_bits[1];
      $password = $line_bits[2];

      $num_valid_letters = 0;
      $letters = Str\chunk($password);
      foreach($letters as $l) {
        if($l === $valid_letter) {
          $num_valid_letters++;
        }
      }

      $bounds = Str\split($range, '-');
      $min = (int)$bounds[0] - 1;
      $max = (int)$bounds[1] - 1;

      $min_contains = false;
      if($min <= C\count($letters) && $letters[$min] === $valid_letter) {
        $min_contains = true;
      }
      $max_contains = false;
      if($max <= C\count($letters) && $letters[$max] === $valid_letter) {
        $max_contains = true;
      }
      if($min_contains || $max_contains) {
        if(!$min_contains || !$max_contains) {
          $valid_passwords++;
        }
      }
    }

    echo('valid pwds '.$valid_passwords."\n");
    return 0;
  }
}