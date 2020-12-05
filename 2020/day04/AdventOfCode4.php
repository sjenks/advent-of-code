<?hh
// @format

final class AdventOfCodeDay4 extends ScriptController {
  <<__Override>>
  protected async function genRun(): Awaitable<int> {
    $required_fields = dict<string, bool>[
      'byr' => false,
      'iyr' => false,
      'eyr' => false,
      'hgt' => false,
      'hcl' => false,
      'ecl' => false,
      'pid' => false,
    ];

    $file = Filesystem::readFile('/data/users/sjenks/www/flib/intern/scripts/analytics/scott/day4/input.txt');
    $split = Str\split($file, "\n");

    $passports = vec[];
    $current_passport = '';
    foreach($split as $s){
      if (Str\length($s) === 0) {
        $passports[] = $current_passport;
        $current_passport = '';
      } else {
        $current_passport = $current_passport. ' ' . $s;
      }
    }

    $valid_passports = 0;
    foreach($passports as $pass) {
      $pass_fields = keyset[];
      $fields = Str\split($pass, ' ');

      $valid = true;
      foreach($fields as $field) {
        $f = Str\split($field, ':');
        $pass_fields[] = $f[0];

        if ($f[0] === 'byr') {
          $byr = (int)$f[1];
          if($byr < 1920 || $byr > 2002) {
            $valid = false;
          }
        } else if ($f[0] === 'iyr') {
          $byr = (int)$f[1];
          if($byr < 2010 || $byr > 2020) {
            $valid = false;
          }
        } else if ($f[0] === 'eyr') {
          $byr = (int)$f[1];
          if($byr < 2020 || $byr > 2030) {
            echo('invalid eyr');
            $valid = false;
          }
        } else if ($f[0] === 'hgt') {
          $hgt = (int)substr($f[1], 0, -2);
          if(static::endsWith($f[1], 'cm')){
            if($hgt < 150 || $hgt > 193) {
              $valid =false;
            }
          } else {
            if($hgt < 59 || $hgt > 76) {
              $valid = false;
            }
          }
        } else if ($f[0] === 'hcl') {
          if(Str\length($f[1]) !== 7) {
            $valid = false;
          }

          if($f[1][0] !== '#') {
            $valid = false;
          }
          // to do add range checks
        } else if ($f[0] === 'ecl') {
          $valid_colors = keyset[
            'amb',
            'blu',
            'brn',
            'gry',
            'grn',
            'hzl',
            'oth',
          ];
          if(!C\contains($valid_colors, $f[1])) {
            $valid = false;
          }
        } else if ($f[0] === 'pid') {
          if(!PHP\is_numeric($f[1])) {
            $valid = false;
          }
          if(Str\length($f[1]) !== 9) {
            $valid = false;
          }
        }
      }

      if(!$valid) {
        continue;
      }

      foreach($required_fields as $key => $_val) {
        if(C\contains($pass_fields, $key)) {
          $required_fields[$key] = true;
        }
      }

      $num_true = 0;
      foreach($required_fields as $key => $val) {
        if($val) {
          $num_true++;
        }
      }
      if($num_true === C\count($required_fields)) {
        $valid_passports++;
      }
      foreach($required_fields as $key => $_val) {
          $required_fields[$key] = false;
      }
    }

    echo('valid passports'.$valid_passports);

    return 0;
  }

  private static function endsWith(string $haystack, string $needle): bool {
    $length = Str\length($needle);
    if (!$length) {
      return true;
    }
    return substr($haystack, -$length) === $needle;
  }
}