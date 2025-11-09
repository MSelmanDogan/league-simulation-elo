import pandas as pd
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[1] / "data"

def load_matches():
    raw = DATA_DIR / "raw" / "matches.csv"
    return pd.read_csv(raw)

def load_elo():
    return pd.read_csv(DATA_DIR / "processed" / "elo.csv")

def save_elo(df):
    processed = DATA_DIR / "processed"
    processed.mkdir(parents=True, exist_ok=True)
    df.to_csv(processed / "elo.csv", index=False)
