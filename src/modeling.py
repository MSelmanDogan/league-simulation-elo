import numpy as np

def win_prob(elo_a, elo_b):
    return 1 / (1 + 10 ** ((elo_b - elo_a) / 400))

def simulate_league(teams, elo_dict, n_sim=10000):
    # round-robin fixtures
    fixtures = [(a, b) for i, a in enumerate(teams) for j, b in enumerate(teams) if i < j]

    points = {team: np.zeros(n_sim) for team in teams}

    for sim in range(n_sim):
        elo_sim = elo_dict.copy()

        for home, away in fixtures:
            p_home = win_prob(elo_sim[home], elo_sim[away])
            rnd = np.random.rand()

            if rnd < p_home:
                points[home][sim] += 3
            else:
                points[away][sim] += 3

    return points
