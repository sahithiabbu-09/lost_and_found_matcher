# Evaluation Harness

Run automated checks with `python -m unittest discover -s tests -v`.

## Five lost/found pair expectations

| Case | Lost details | Found details | Expected |
|---|---|---|---|
| 1 | Black Samsung phone, library | Black Samsung phone, library | likely |
| 2 | Blue bottle | Blue bottle | possible |
| 3 | Red bottle | Blue bottle | none (colour conflict) |
| 4 | Black phone | Black wallet | none (item conflict) |
| 5 | Black phone, dated 2026-10-05 | Black phone, dated 2026-12-10 | none (over 30 days) |

## Red-team cases
See `tests/red_team_cases.csv`. Record the actual output after running the LLM-enabled version. The local fallback does not prove LLM prompt-injection resistance; verify with your chosen model and report the results honestly.
