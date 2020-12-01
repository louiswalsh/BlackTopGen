import database_generator, calculator_service

print('\n\n\n//=====================================================//')
print('                Welcome to BlackTopGen \n')
print('  In this program, we will be creating two 2K19 blacktop')
print('    teams that are evenly matched. Author: Louie Walsh')
print('//=====================================================//')


def user_input_rating():
    print('\n.........................................................')
    overall = int(input('        Enter your overall desired rating: '))
    sze = int(input('        Enter number of players on each team: '))
    print('  Generating two teams with the overall rating of ' + str(overall))
    print('.........................................................\n')

    return overall, sze


def team_name_input():
    print('\n.........................................................')
    team1 = input('                  Team 1 Name: ')
    team2 = input('                  Team 2 Name: ')
    print('.........................................................\n')


# teamNameInput()
ovr, size = user_input_rating()

print('\n.........................................................')
print('           Creating Player Database')
database_generator.createPlayerTable()
print('                   Created')
print('.........................................................\n')


print('\n.........................................................')
print('      Matching Players to the following ratings')
team_arrays = calculator_service.gen_rtg_arrays(int(ovr), int(size))
print('.........................................................\n')


print('\n.........................................................')
print('Team 1:')
for rtg in team_arrays[0]:
    database_generator.selectPlayerByRtg(rtg)
print('.........................................................\n')

print('\n.........................................................')
print('Team 2:')
for rtg in team_arrays[1]:
    database_generator.selectPlayerByRtg(rtg)
print('.........................................................\n')
