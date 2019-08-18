
def print_server_stats(all_profession_names, profession_count):
    if IsOutputToConsole:
        professions = ['Четвёртые', 'Третьи', 'Вторые', 'Первые']
        for i in range(len(all_profession_names)):
            print('')
            print(('################# ' + professions[i] + ' профессии' + ' #################').center(100))
            print('')
            for j in range(len(all_profession_names[i])):
                print('' + (str(all_profession_names[i][j]).ljust(30) + ' ' + str(profession_count[i][j]).rjust(
                    5)).center(100))

