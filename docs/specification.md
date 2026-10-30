# One-page Specification: Lost and Found Matcher

## Purpose
Suggest possible matches between campus lost-item reports and found-item reports so the help desk can review candidates faster. The tool never determines ownership.

## Inputs
Two UTF-8 CSV files, each with at least 10 rows:
- `data/lost.csv`
- `data/found.csv`

Required columns: `id,date,report`. Dates use `YYYY-MM-DD`.

## Extraction output
For each report, the LLM returns JSON with `item`, `colour`, `brand`, `place`, and `summary`. Item must be one of: phone, wallet, id_card, bottle, bag, earphones, keys, umbrella, calculator, watch, spectacles, other. Colour must be one of ten allowed colours or null. Brand is as written or null. Place is a recognized campus place or null. Summary is at most eight words and contains no names.

## Validation and fact checks
Python validates the schema. Colour, brand, and place are retained only if they appear in the report text. Missing facts are null. LLM output is parsed defensively; if extraction fails, a simple local fallback is used.

## Matching rules
- Item must be the same; `other` never matches automatically.
- Reports more than 30 days apart are rejected.
- If both reports specify a colour and colours differ, reject.
- If both reports specify a brand and brands differ, reject.
- Same colour adds 2 points, same brand adds 2, same place adds 1.
- Score 3 or more = likely; score 1–2 = possible; score 0 is not listed.
- Every lost report is compared with every found report. Results are sorted best first.
- A found item suggested for more than one lost report is flagged as a double claim.

## Outputs
`outputs/matches.csv`, `outputs/no_match.csv`, `outputs/unclaimed.csv`, and `outputs/summary.txt`.

## Human checkpoint
Before handing over an item, the help desk asks the claimant for a detail not included in either report. A score is only a suggestion, not proof of ownership.
