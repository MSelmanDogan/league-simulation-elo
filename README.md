# League Simulation & Match Prediction (Monte Carlo + Elo)

Simulate league outcomes using Elo strengths and xG-derived probabilities; visualize final standings distributions.

## What you'll find
- Elo rating computation and updates
- Match outcome simulation (10k+ runs)
- Probability distributions and summary plots

## Quick start
```bash
python -m venv .venv && source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
jupyter lab  # or jupyter notebook
```

## Repository structure
```
league-simulation-elo/
├── data/
│   ├── raw/           # downloaded datasets (gitignored)
│   ├── processed/     # feature tables / model-ready (gitignored)
│   └── external/      # third-party data (gitignored)
├── notebooks/
│   ├── 01_data_prep.ipynb
│   ├── 02_modeling.ipynb
│   └── 03_evaluation_and_viz.ipynb
├── src/
│   ├── __init__.py
│   ├── data.py        # loading / cleaning
│   ├── features.py    # feature engineering
│   ├── modeling.py    # training / evaluation
│   └── viz.py         # plots / dashboards
├── requirements.txt
├── LICENSE (MIT)
└── README.md
```

# League Simulation & Match Prediction (Monte Carlo + Elo Ratings)

This project simulates a football league using Elo-based team strengths and Monte Carlo simulations.  
It predicts final standings, point distributions, and outcome probabilities across thousands of simulated seasons.

The purpose is to demonstrate a reproducible, data–driven approach for league prediction using open data and simple modeling techniques.

---

## ✅ What This Project Does
- Builds initial Elo ratings from historical match results
- Runs thousands of simulated seasons (Monte Carlo)
- Applies probability-based win prediction using Elo differences
- Produces final league tables and point distributions
- Visualizes outcomes for interpretation (histograms, mean standings)

---

## ✅ Data Requirements
Provide a CSV file at:
data/raw/matches.csv


### Example:
home_team,away_team,home_goals,away_goals
Barcelona,Real Madrid,1,2
Arsenal,Chelsea,3,1
Fenerbahçe,Galatasaray,2,2

## Tools
- Python, NumPy, Pandas, Matplotlib

## License
MIT — see `LICENSE`.
