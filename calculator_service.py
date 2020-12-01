import random
from functools import reduce


def gen_avg(expected_avg, team_size):
    n = team_size
    a = 65
    b = 98
    while True:
        lt = [random.randint(a, b) for i in range(n)]
        avg = reduce(lambda x, y: x + y, lt) / len(lt)

        if avg == expected_avg:
            return lt


def gen_rtg_arrays(expected_avg, team_size):
    team1_rtgs = []
    team2_rtgs = []
    condition = 0
    while condition == 0:
        team1_rtgs = gen_avg(expected_avg, team_size)
        team2_rtgs = gen_avg(expected_avg, team_size)

        dups = set(team1_rtgs) & set(team2_rtgs)

        if dups.__len__() == 0:
            condition = 1

    teams_rtgs = [team1_rtgs, team2_rtgs]
    print('    ', teams_rtgs)
    return teams_rtgs


