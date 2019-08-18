
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

