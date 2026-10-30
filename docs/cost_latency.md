# Cost and Latency Note

## API call count
The program attempts one LLM call per report. For 10 lost and 10 found reports, one full run makes up to 20 extraction calls. Matching itself is plain Python and does not call the API. If a call fails, the program uses its local fallback.

## Latency
Latency depends on the selected model, network, rate limits and report length. Measure it in the target environment rather than assuming a fixed number. The program prints total extraction time for a run; divide by the number of reports for a rough per-report average.

## Cost
Actual cost depends on the chosen model, token usage and current provider pricing. This starter project does not hard-code a price. Check the provider's current pricing and usage dashboard before reporting a monetary estimate. With no API key configured, API cost is zero because the local fallback is used.

## Reporting template
- Reports processed: ___
- API calls attempted: ___
- Total extraction time: ___ seconds
- Average per report: ___ seconds
- Model and date checked: ___
- Estimated cost: ___ (state pricing source and date)
