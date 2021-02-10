import xlrd
from collections import OrderedDict
import simplejson as json
import os
import random
from functools import reduce

# Open the workbook and select the first worksheet
wb = xlrd.open_workbook('W:\\PersonalProjects\\BlackTopGen\\blacktop_server\\2K19_Players.xlsx')
sh = wb.sheet_by_index(0)


# List to hold dictionaries
data_list = []


# Iterate through each row in worksheet and fetch values into dict
for rownum in range(1, sh.nrows):
    data = OrderedDict()
    row_values = sh.row_values(rownum)
    data['id'] = row_values[0]
    data['name'] = row_values[1]
    data['rating'] = row_values[2]
    data_list.append(data)

    # Serialize the list of dicts to JSON
j = json.dumps(data_list)
d = json.loads(j)


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

    str1 = ''.join(str(e) for e in teams_rtgs)
    return str1


def function(rating):
    for item in d:
        if rating == item['rating']:
            print("Name: {}\n Rating: {}\n".format(item['name'],item['rating']))



function(80)