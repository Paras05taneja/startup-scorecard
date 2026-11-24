# Startup Screening Scorecard

A short Python script that ranks startups with a weighted scorecard and labels each one **Meet**, **Watch** or **Pass**. It shows how an analyst can screen many deals consistently.

**Author:** Paras Taneja

## How it works
Each startup is scored 1-5 on five criteria. The weights reflect what early-stage investors usually stress most:

| Criterion | Weight |
|---|---|
| Team | 30% |
| Market | 25% |
| Traction | 20% |
| Product | 15% |
| Business model | 10% |

Score >= 3.5 is **Meet**, 2.5-3.5 is **Watch**, below 2.5 is **Pass**.

## Data
`startups.csv` contains **fictional example companies** with made-up scores. Replace them with real startups and your own scores, and change the weights in `scorecard.py` to match your thesis.

## Run
```bash
pip install pandas
python scorecard.py
```
Output: a ranked table in the terminal and `ranked_startups.csv`.

## Limitations
Scores are subjective, and a weighted average hides important nuances. Use it to organise a first screen, not to make the final investment decision.

## License
MIT
