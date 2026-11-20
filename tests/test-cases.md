# Test cases

Worked out by hand first (Testing Lead), then checked in the tool on every release.
Answers are Q1 → Q20: Y = Yes, P = Partly, N = No.

| Case | Business type | Answers | Expected score | Band | Top actions (in order) |
|---|---|---|---|---|---|
| A | Well-prepared shop | YYYYYYYYYYYYYYYYYYYY | 100 | Good | none |
| B | Typical café | PNNYPYNNPNPNNYNNYYNP | 38.5 | At risk | Q7, Q12, Q2, Q3, Q8 |
| C | No backups, rest good | NNNYYYYYYYYYYYYYYYYY | 82 | Good | Q1, Q2, Q3 |
| D | Starting from zero | NNNNNNNNNNNNNNNNNNNN | 0 | At risk | Q1, Q7, Q4, Q6, Q12 |
| E | Secure but weak online | YYPYYYYYYYYYYYYYYNNN | 82.5 | Good | Q18, Q19, Q20, Q3 |

## Rules being tested
- Yes = full points, Partly = half, No = 0 (total 100)
- 80+ Good · 50–79.5 Needs work · below 50 At risk
- Top 5 = most points lost; tie → higher-points question first, then lower question number
- Only real gaps are listed (case E shows 4 actions)

## Results
| Version | Date | Where | Result |
|---|---|---|---|
| v1 | 11 Nov | Laptop | 3/5 – tie-break bug (D), extra action (E) |
| v1.1 | 11 Nov | Laptop | 5/5 |
| v1.2 | 17 Nov | Laptop and phone sizes | 10/10 + print view |
| v1.3 | 20 Nov | Live site, Chrome | 5/5 + copy |
| v1.4 | 20 Nov | Phone, iPad and laptop sizes | 15/15 |
| v1.4 | – | Real phone / iPad | to do (Testing Lead) |

Automated check: `python tests/test_prototype.py` (see the file for setup).
