# RigReceipts Freight Economics — canonical semantics

## Offered-load metrics

- loaded RPM = offered pay / loaded miles
- all-mile RPM = offered pay / (loaded miles + deadhead miles)

## Weekly economic floor

- weekly break-even cost = weekly fixed costs + (variable CPM × projected total weekly miles)
- break-even all-mile RPM = weekly break-even cost / projected total weekly miles

## Weekly revenue target

- weekly revenue needed = weekly break-even cost + desired weekly driver pay + desired weekly reserve
- target all-mile RPM = weekly revenue needed / projected total weekly miles
- target loaded RPM = weekly revenue needed / expected loaded weekly miles

## Specific-offer verdict

- ACCEPT: offered all-mile RPM >= target all-mile RPM
- COUNTER: offered all-mile RPM >= break-even all-mile RPM but < target all-mile RPM
- PASS: offered all-mile RPM < break-even all-mile RPM

Target loaded RPM is preserved as a planning metric only. It never controls the specific-load verdict.
