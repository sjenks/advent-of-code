<?hh
// @format

final class AdventOfCode6 extends ScriptController {

  <<__Override>>
  protected async function genRun(): Awaitable<int> {
    $file = Filesystem::readFile(
      '/data/users/sjenks/www/flib/intern/scripts/analytics/aoc-06/input.txt',
    );
    $lines = Str\split($file, "\n");


    $bag_map = dict[];
    foreach($lines as $line) {
      if(Str\length($line) < 2) {
        continue;
      }
      $sentence = Str\split($line, 'contain');
      $smaller_bags = Str\split($sentence[1], ',');
      $smaller_bags_stripped = Vec\map($smaller_bags, ($a) ==> static::clean($a));
      $left = static::clean($sentence[0]);
      $bag_map[$left] = $smaller_bags_stripped;
    }

    // $possible_start_bags = 0;
    // foreach($bag_map as $key => $_val) {
    //   if(static::canContainGoldBag($bag_map, $key)) {
    //     //echo("$key \n");
    //     $possible_start_bags++;
    //   }
    // }
    // echo($possible_start_bags);
    $bags_required = static::numContained($bag_map, 'shiny gold', 0);
    echo($bags_required);

    return 1;
  }

  private static function canContainGoldBag(dict<string, vec<string>> $bag_map, string $current_bag): bool {
    if(!C\contains_key($bag_map, $current_bag)) {
      return false;
    }
    $bags = $bag_map[$current_bag];
    $matches = vec[];

    foreach ($bags as $bag) {
      $_num = Str\split($bag, ' ')[0];
      $bag = static::removeNums($bag);
      if (Str\contains($bag, 'shiny gold')) {
        return true;
      } else if (Str\contains($bag, 'no other')) {
        $matches[] = false;
      } else {
        $matches[] = static::canContainGoldBag($bag_map, $bag);
      }
    }
    foreach($matches as $m) {
      if($m){
        return true;
      }
    }
    return false;
  }

  private static function numContained(dict<string, vec<string>> $bag_map, string $current_bag, int $num_bags): int {
    if(!C\contains_key($bag_map, $current_bag)) {
      return 0;
    }
    $bags = $bag_map[$current_bag];
    $matches = vec[];

    foreach ($bags as $bag) {
      $num = (int)Str\split($bag, ' ')[0];
      $bag = static::removeNums($bag);
      if ($bag === 'no other') {
        return 1;
      } else {
        $num_contained = static::numContained($bag_map, $bag, $num_bags);
        echo("$bag $num $num_contained \n");
        $matches[] = ($num * $num_contained);
      }
    }
    $total = 1;
    foreach($matches as $m) {
      $total += $m;
    }
    return $total;
  }

  private static function clean(string $in): string{
    $in = Str\replace($in, '.', '');
    $in = Str\replace($in, 'bags', '');
    $in = Str\replace($in, 'bag', '');
    return Str\trim($in);
  }

  private static function removeNums(string $in): string{
    $in = Str\replace($in, '0', '');
    $in = Str\replace($in, '1', '');
    $in = Str\replace($in, '2', '');
    $in = Str\replace($in, '3', '');
    $in = Str\replace($in, '4', '');
    $in = Str\replace($in, '5', '');
    $in = Str\replace($in, '6', '');
    $in = Str\replace($in, '7', '');
    $in = Str\replace($in, '8', '');
    $in = Str\replace($in, '9', '');
    return Str\trim($in);
  }
}
