import random
from functools import reduce


def gen_avg(expected_avg=89, n=5, a=65, b=98):
    while True:
        lt = [random.randint(a, b) for i in range(n)]
        avg = reduce(lambda x, y: x + y, lt) / len(lt)

        if avg == expected_avg:
            return lt


def gen_rtg_arrays():
    team1_rtgs = []
    team2_rtgs = []
    condition = 0
    while condition == 0:
        team1_rtgs = gen_avg()
        team2_rtgs = gen_avg()

        dups = set(team1_rtgs) & set(team2_rtgs)

        if dups.__len__() == 0:
            condition = 1

    teams_rtgs = [team1_rtgs, team2_rtgs]

    return teams_rtgs


gen_rtg_arrays()
