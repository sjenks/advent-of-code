<?hh
// @format

final class AdventOfCodeDay5 extends ScriptController {
  <<__Override>>
  protected async function genRun(): Awaitable<int> {
    $file = Filesystem::readFile(
      '/data/users/sjenks/www/flib/intern/scripts/analytics/scott/day5/input.txt',
    );
    $lines = Str\split($file, "\n");
    $maxSeatId = 0;
    $allSeatIds = vec[];
    foreach ($lines as $seat) {
      if (Str\length($seat) < 1) {
        continue;
      }
      $row = static::getRow(substr($seat, 0, 7));
      $col = static::getCol(substr($seat, 7, 3));
      $seatId = ($row * 8) + $col;
      $allSeatIds[] = $seatId;
      if ($seatId > $maxSeatId) {
        $maxSeatId = $seatId;
      }
    }
    PHP\sort(inout $allSeatIds);
    for($i = 1; $i < C\count($allSeatIds); $i++) {
      if($allSeatIds[$i-1] == $allSeatIds[$i] - 2) {
        echo($allSeatIds[$i-1] .' '. $allSeatIds[$i] . "\n" );
      }
    }

    echo('max seat id'.$maxSeatId);

    return 0;
  }

  private static function getRow(string $letters): int {
    $letters = PHP\str_replace('F', '0', $letters);
    $letters = PHP\str_replace('B', '1', $letters);
    return (int)PHP\bindec($letters);
  }

  private static function getCol(string $letters): int {
    $letters = PHP\str_replace('L', '0', $letters);
    $letters = PHP\str_replace('R', '1', $letters);
    return (int)PHP\bindec($letters);
  }
}
