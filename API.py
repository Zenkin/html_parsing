import os
import sys

ServersName = ['Blackbird', 'Esthus', 'Airin', 'Elcardia']
URL = 'http://l2on.net/?c=userdata&a=pledge&world='
IsOutputToConsole = True


def clear_screen():
    if sys.platform == 'win32':
        os.system('cls')
    else:
        os.system('clear')


def get_full_url(server_number):
    return str(URL + ServersName[int(server_number) - 1])


def get_server_number():
    clear_screen()

    print('#########   HELLO MY FRIEND   ##########'.center(100))
    print("######### LET's START PARSING ##########".center(100))
    print('Choose server: '.center(100))
    numb = 1
    for ServerName in ServersName:
        print(('(' + str(numb) + ')' + ServerName).center(100))
        numb += 1

    server_number = input('Server number _'.rjust(30))

    return int(server_number)


def choose_clan():
    print('')
    selected_clan_number = input('Choose clan( 1-50):'.rjust(30))
    if IsOutputToConsole:
        clear_screen()

    return int(selected_clan_number)


def print_top_50(top_50_clans_information, server_number):
    if IsOutputToConsole:
        print(('############# Top 50 clans of ' + ServersName[int(server_number) - 1] + ' #############').center(100))
        for i in range(51):
            print(top_50_clans_information[0][i].center(4), top_50_clans_information[1][i].rjust(4),
                  top_50_clans_information[2][i].ljust(15), top_50_clans_information[4][i].center(15),
                  top_50_clans_information[5][i].ljust(20), top_50_clans_information[6][i].ljust(20),
                  top_50_clans_information[7][i].ljust(5), top_50_clans_information[8][i])


def print_clan_information(clan_header_title, clan_header_data,
                           table_with_member_data, top_50_clans_information,
                           selected_clan_number):
    if IsOutputToConsole:

        member_names = table_with_member_data[0]
        member_titles = table_with_member_data[1]
        member_classes = table_with_member_data[2]
        member_races = table_with_member_data[3]
        member_lvls = table_with_member_data[4]
        member_updates = table_with_member_data[5]

        name_of_the_selected_clan = top_50_clans_information[2]
        print(('############# '
               + name_of_the_selected_clan[int(selected_clan_number)]
               + "'s CLAN INFO #############"
               ).center(100)
              )
        for i in range(len(clan_header_title)):
            print('                      ' + clan_header_title[i] + ' ' + clan_header_data[i])
        print('############ СОСТАВ ############'.center(100))
        for i in range(len(table_with_member_data[0])):
            print(''.ljust(4) + member_names[i].ljust(20) + member_titles[i].ljust(20) + member_classes[i].ljust(30) +
                  member_races[i].ljust(15) + member_lvls[i].ljust(10) + member_updates[i].ljust(20))


def print_clan_stats(clan_races, clan_race_counts, clan_races_ratio,
                     clan_classes, clan_class_counts, clan_classes_ratio,
                     clan_lvls, clan_lvl_counts, clan_lvls_ratio):
    if IsOutputToConsole:
        print('')
        print('############# Races Stats #############'.center(100))
        for i in range(len(clan_races)):
            print(str(clan_races[i]).ljust(30) + str(clan_race_counts[i]).ljust(15) + str(clan_races_ratio[i]))
        print('')
        print('############# Classes Stats #############'.center(100))
        for i in range(len(clan_classes)):
            print(str(clan_classes[i]).ljust(30) + str(clan_class_counts[i]).ljust(15) + str(clan_classes_ratio[i]))
        print('')
        print('############# LvLs Stats #############'.center(100))
        for i in range(len(clan_lvls)):
            print(str(clan_lvls[i]).ljust(30) + str(clan_lvl_counts[i]).ljust(15) + str(clan_lvls_ratio[i]))


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


def print_server_pofession_stats(first_profession, second_profession, percentages):
    if IsOutputToConsole:
        for i in range(len(second_profession[0])):
            print(first_profession[i*3])
            print(second_profession[0][i].ljust(25) + ' '
                  + second_profession[1][i].ljust(25) + ' '
                  + second_profession[2][i].ljust(25)
                  )
            print(str(percentages[0][i]).ljust(25) + ' '
                  + str(percentages[1][i]).ljust(25) + ' '
                  + str(percentages[2][i]).ljust(25)
                  )
            print('')
