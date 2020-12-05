<?hh
// @format

final class AdventOfCodeDay3 extends ScriptController {
  <<__Override>>
  protected async function genRun(): Awaitable<int> {
    $file = Filesystem::readFile('/data/users/sjenks/www/flib/intern/scripts/analytics/scott/day3/input.txt');
    $split = Str\split($file, "\n");

    $grid = vec[];
    foreach($split as $s){
      if (Str\length($s) > 1) {
        $grid[] = Str\chunk($s);
      }
    }

    $max_x = C\count($grid[0]);
    $cur_x = 0;
    $tree_count = 0;
    for ($cur_y = 0; $cur_y < C\count($grid); $cur_y+=2) {
      if($grid[$cur_y][$cur_x] === '#') {
        $tree_count++;
      }
      $cur_x += 1;
      $cur_x = $cur_x % $max_x;
    }
    echo($tree_count . "\n");

    return 0;
  }
}