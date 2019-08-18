
import pars as parsing
import API
import GoogleDocAPI as GoogleDoc

server_number = API.get_server_number()
full_url_name = API.get_full_url(server_number)

top_50_clans_information = parsing.get_top_50(full_url_name)
API.print_top_50(top_50_clans_information, server_number)

id_of_clans = top_50_clans_information[3]
selected_clan_number = API.choose_clan()
clan_id = id_of_clans[selected_clan_number-1]

clan_header_title, clan_header_data, table_with_member_data = parsing.get_clan_info(clan_id)

clan_header = [clan_header_title, clan_header_data]

API.print_clan_information(clan_header_title,
                           clan_header_data,
                           table_with_member_data,
                           top_50_clans_information,
                           selected_clan_number
                           )

member_names = table_with_member_data[0]
member_titles = table_with_member_data[1]
member_classes = table_with_member_data[2]
member_races = table_with_member_data[3]
member_lvls = table_with_member_data[4]
member_updates = table_with_member_data[5]

all_member_data = [member_names, member_titles, member_classes, member_races, member_lvls, member_updates]

ClanStatistics = parsing.get_clans_statistics(all_member_data)

clan_races = ['Рассы']
clan_race_counts = ['Количество']
clan_races_ratio = ['Процент']
clan_races.extend(ClanStatistics[0])
clan_race_counts.extend(ClanStatistics[1])
clan_races_ratio.extend(ClanStatistics[2])

races_data = [clan_races, clan_race_counts, clan_races_ratio]

clan_classes = ['Классы']
clan_class_counts = ['Количество']
clan_classes_ratio = ['Процент']
clan_classes.extend(ClanStatistics[3])
clan_class_counts.extend(ClanStatistics[4])
clan_classes_ratio.extend(ClanStatistics[5])

classes_data = [clan_classes, clan_class_counts, clan_classes_ratio]

clan_lvls = ['Лвл']
clan_lvl_counts = ['Количество']
clan_lvls_ratio = ['Проценты']
clan_lvls.extend(ClanStatistics[6])
clan_lvl_counts.extend(ClanStatistics[7])
clan_lvls_ratio.extend(ClanStatistics[8])

clan_lvl_data = [clan_lvls, clan_lvl_counts, clan_lvls_ratio]

API.print_clan_stats(clan_races, clan_race_counts, clan_races_ratio,
                     clan_classes, clan_class_counts, clan_classes_ratio,
                     clan_lvls, clan_lvl_counts, clan_lvls_ratio)

all_profession_names, profession_count = parsing.get_server_stats(server_number-1)

first_profession_name = all_profession_names[3]
second_profession_name = all_profession_names[2]
third_profession_name = all_profession_names[1]
fourth_profession_name = all_profession_names[0]

first_profession_counts = profession_count[3]
second_profession_counts = profession_count[2]
third_profession_counts = profession_count[1]
fourth_profession_counts = profession_count[0]

first_profession_data = [first_profession_name, first_profession_counts]
second_profession_data = [second_profession_name, second_profession_counts]
third_profession_data = [third_profession_name, third_profession_counts]
fourth_profession_data = [fourth_profession_name, fourth_profession_counts]

API.print_server_stats(all_profession_names, profession_count)

first_profession, second_profession, percentages = parsing.get_profession_stats(all_profession_names,
                                                                                profession_count)

API.print_server_pofession_stats(first_profession, second_profession, percentages)

GoogleDoc.load_all_data_in_google_doc(clan_header, all_member_data,
                                      races_data, classes_data,
                                      clan_lvl_data, first_profession_data,
                                      second_profession_data, third_profession_data,
                                      fourth_profession_data, first_profession,
                                      second_profession, percentages)

