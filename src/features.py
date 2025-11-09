def update_elo(elo, home, away, home_goals, away_goals, k=20):
    if home_goals > away_goals:
        result = 1
    elif home_goals < away_goals:
        result = 0
    else:
        result = 0.5

    exp = 1 / (1 + 10 ** ((elo[away] - elo[home]) / 400))
    elo[home] += k*(result-exp)
    elo[away] -= k*(result-exp)
    return elo
