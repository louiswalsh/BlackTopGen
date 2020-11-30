import database_generator

print('\n\n\n//=====================================================//')
print('                Welcome to BlackTopGen \n')
print('  In this program, we will be creating two 2K19 blacktop')
print('    teams that are evenly matched. Author: Louie Walsh')
print('//=====================================================//')


def userInputRating():
    print('\n\n.........................................................')
    print('.........................................................')
    overall = input('        Enter your overall desired rating: ')
    print('  Generating two teams with the overall rating of ' + overall)
    print('.........................................................')
    print('.........................................................\n\n\n')

    #TODO: Special cases of max/min avg's of the top 10 and bottom 10 players


def teamNameInput():
    print('\n\n.........................................................')
    print('.........................................................')

    team1 = input('                  Team 1 Name: ')
    team2 = input('                  Team 2 Name: ')
    print('.........................................................')
    print('.........................................................\n\n\n')


teamNameInput()
userInputRating()