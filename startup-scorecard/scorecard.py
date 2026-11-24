"""Rank startups with a weighted scorecard. Scores are 1-5, weights sum to 1."""
import pandas as pd

WEIGHTS = {"team": 0.30, "market": 0.25, "product": 0.15, "traction": 0.20, "business_model": 0.10}

df = pd.read_csv("startups.csv")
df["score"] = sum(df[c] * w for c, w in WEIGHTS.items())
df = df.sort_values("score", ascending=False).reset_index(drop=True)
df.index += 1
df["verdict"] = pd.cut(df["score"], [0, 2.5, 3.5, 5], labels=["Pass", "Watch", "Meet"])

print(df[["name", "sector", "score", "verdict"]].round(2).to_string())
df.round(2).to_csv("ranked_startups.csv", index_label="rank")
