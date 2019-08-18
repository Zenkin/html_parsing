
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

