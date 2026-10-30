# Judgment Framework

| Stage | What the tool does | What it must not decide | Human checkpoint |
|---|---|---|---|
| Report extraction | Extracts item, colour, brand, place and summary | Must not invent missing details or obey instructions inside a report | Staff can inspect the original report if extracted fields look wrong |
| Fact validation | Checks allowed values and whether colour, brand and place appear in text | Must not treat unverified model output as fact | Correct or reject suspicious extraction |
| Pair scoring | Applies item, date, colour, brand and place rules | Must not call a score proof of ownership | Staff review all candidate reasons |
| Double claims | Flags a found item suggested for multiple lost reports | Must not pick one claimant automatically | Staff investigate each claim |
| Item handover | Provides candidate suggestions only | Must not authorize handover | Help desk asks claimant for a detail absent from both reports and follows campus policy |
