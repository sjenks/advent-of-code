from z3 import *

f = open("inputrules.txt", "r")
lines = f.read().split("\n")
lines = [l for l in lines if len(l) > 0]

def parse_range(s):
  l, h = s.split("-")
  return (int(l), int(h))

rules = {}
for line in lines:
  n, d = line.split(": ")
  r1, r2 = d.split(" or ")
  rules[n] = [parse_range(r1), parse_range(r2)]

bad = []
validtickets = []
f = open("tickets.txt", "r")
lines = f.read().split("\n")
lines = [l for l in lines if len(l) > 0]
for line in lines:
  vs = line.split(",")
  valid = True
  for v in vs:
    v = int(v)
    ok = False
    for rule in rules.values():
      for l, h in rule:
        if v >= l and v <= h:
          ok = True
    if not ok:
      bad.append(v)
      valid = False
  if valid:
    validtickets.append(vs)
print(sum(bad))

solver = Solver()
ps = [Int(f"p{i}") for i in range(len(rules))]
solver.add(Distinct(*ps))
for p in ps:
  solver.add(p >= 0)
  solver.add(p < len(rules))

for ticket in validtickets:
  for i, v in enumerate(ticket):
    v = int(v)
    for ri, rule in enumerate(rules.values()):
      r1, r2 = rule
      r1l, r1h = r1
      r2l, r2h = r2
      solver.add(Implies(ps[ri] == i, Or(
        And(v >= r1l, v <= r1h),
        And(v >= r2l, v <= r2h)
      )))

assert solver.check() == sat
m = solver.model()

myticket = [197,173,229,179,157,83,89,79,193,53,163,59,227,131,199,223,61,181,167,191]
acc = 1
for i, n in enumerate(rules.keys()):
  if not n.startswith("departure"):
    continue
  ti = m.eval(ps[i]).as_long()
  acc *= myticket[ti]
print(acc)
