# Lost and Found Matcher

A console-based Python tool that extracts details from campus lost/found reports and suggests possible matches. It uses Python rules for comparison and does **not** decide ownership.

## Features

- Reads `data/lost.csv` and `data/found.csv` (10 sample reports each).
- Extracts item, colour, brand, place, and a short summary.
- Optional Gemini API integration; a local rule-based fallback keeps the demo runnable without a key.
- Checks that extracted colour, brand, and place occur in the original report.
- Rejects item mismatches, conflicting colours/brands, `other` items, and reports more than 30 days apart.
- Scores matches: same colour +2, same brand +2, same place +1. Scores 3+ are `likely`; scores 1–2 are `possible`.
- Writes `matches.csv`, `no_match.csv`, `unclaimed.csv`, and `summary.txt` in `outputs/`.
- Flags found items suggested for multiple lost reports.

## Requirements

- Python 3.10+
- Optional: Gemini API key for LLM extraction

## Run locally

1. Download/unzip this repository.
2. Open a terminal in the project folder.
3. (Optional but recommended) Create a virtual environment:

   ```bash
   python -m venv .venv
   ```

   Windows PowerShell:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

   macOS/Linux:

   ```bash
   source .venv/bin/activate
   ```

4. Install dependencies (only needed for Gemini API use):

   ```bash
   pip install -r requirements.txt
   ```

5. (Optional) Set your Gemini API key in the terminal. Do not put it in `app.py` or commit it.

   Windows PowerShell:
   ```powershell
   $env:GEMINI_API_KEY="YOUR_KEY_HERE"
   $env:GEMINI_MODEL="gemini-2.5-flash"
   ```

   macOS/Linux:
   ```bash
   export GEMINI_API_KEY="YOUR_KEY_HERE"
   export GEMINI_MODEL="gemini-2.5-flash"
   ```

6. Run:

   ```bash
   python app.py
   ```

Without `GEMINI_API_KEY`, the program uses a basic local fallback. This is useful for a first demo, but its extraction is less capable than an LLM.

## Output files

- `outputs/matches.csv`: candidate pairs sorted by score, with reasons.
- `outputs/no_match.csv`: lost reports with no suggested candidate.
- `outputs/unclaimed.csv`: found reports not suggested for any lost report.
- `outputs/summary.txt`: counts, double claims, and the human verification reminder.

## Human verification checkpoint

A suggested match is not proof of ownership. Before handing over an item, the help desk must ask the claimant to provide a detail that does not appear in either report.

## Testing

Run the test suite:

```bash
python -m unittest discover -s tests -v
```

## Project files

```text
lost-found-matcher/
├── app.py
├── data/
│   ├── lost.csv
│   └── found.csv
├── outputs/                 # generated output files
├── tests/
│   └── test_matcher.py
├── docs/
│   ├── specification.md
│   ├── judgment_framework.md
│   ├── cost_latency.md
│   ├── ai_decision_journal.md
│   └── reflection_template.md
├── system_prompt.txt
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## GitHub upload

Create a new repository on GitHub, then upload the contents of this folder. Do not upload `.env`, real API keys, or virtual environment folders. For meaningful commit history, use Git locally and make separate commits for the initial structure, matching rules/tests, and documentation/outputs.

## Included demo data
The repository includes 10 sample lost reports, 10 sample found reports, and example output files generated using the local fallback. Run the app again to regenerate them.
