#!/usr/bin/env python3

import urllib.request

from bs4 import BeautifulSoup

IsOutputToConsole = True
ServersName = ['Blackbird', 'Esthus', 'Airin', 'Elcardia']

URL = 'http://l2on.net/?c=userdata&a=pledge&world='


def get_html_code(site_url):
    open_url = urllib.request.urlopen(site_url)
    html_code = open_url.read()
    return html_code


def get_url_from_str(string):
    return string[string.find('/'):string.rfind('"')]


def get_count_from_str(string):
    return string[string.find('(') + 1:string.rfind(')')]


def get_id(string):
    return string[string.find('id=') + 3:string.rfind('"')]


def is_in_html_code(html_code, obj):
    flag = False
    for content in html_code.find(class_='values').find_all('a'):
        if content.contents[0] is not None:
            content = content.contents[0]
        if str(content) == str(obj):
            flag = True
    return flag


def get_name_of_th(html_code):
    th_code = html_code.find('th')
    if th_code.find('a') is not None:
        return str(th_code.find('a').contents[0] + ':')
    else:
        return str(th_code.contents[0])


def get_clan_info(clan_id):
    html_code = BeautifulSoup(get_html_code('http://l2on.net/?c=userdata&a=pledge&id=' + clan_id), 'html.parser')
    clan_header_titles, clan_header_all_data = get_header_info(html_code)
    all_members_data = get_members_table(html_code)

    return clan_header_titles, clan_header_all_data, all_members_data


def is_title(td_blocks_content):
    if td_blocks_content.find(class_='add') is not None:
        return True
    else:
        return False


def get_obj_info(clan_member_obj):
    checked_obj = []
    obj_name = []
    obj_counts = []
    for number_i in range(len(clan_member_obj) - 1):
        obj_count = 0
        current_obj = clan_member_obj[number_i + 1]
        if not_in_list(current_obj, checked_obj):
            checked_obj.append(current_obj)
            for number_j in range(len(clan_member_obj)):
                if clan_member_obj[number_j] == current_obj:
                    obj_count += 1
            obj_name.append(current_obj)
            obj_counts.append(obj_count)
    return obj_name, obj_counts


def not_in_list(current_obj, checked_obj):
    for name in checked_obj:
        if name == current_obj:
            return False
    return True


def get_calns_position(td_tag_content, positions_all_of_clans):
    clans_position_in_list = str(td_tag_content.find('span').contents[0])
    positions_all_of_clans.append(clans_position_in_list)
    return positions_all_of_clans


def get_clans_symbol_of_position(td_tag_content, all_of_clans_position_symbols):
    if td_tag_content.find('span').find(class_='dif-no') is not None:
        all_of_clans_position_symbols.append('  ')
    if td_tag_content.find('span').find(class_='dif-up') is not None:
        clans_position_symbol = td_tag_content.find('span').find(class_='dif-up').contents[0]
        all_of_clans_position_symbols.append(clans_position_symbol)
    if td_tag_content.find('span').find(class_='dif-down') is not None:
        clans_position_symbol = td_tag_content.find('span').find(class_='dif-down').contents[0]
        all_of_clans_position_symbols.append(clans_position_symbol)
    return all_of_clans_position_symbols


def get_clans_alliance(td_tag_content, all_of_clans_alliance_name):
    if td_tag_content.find('a') is not None:
        all_of_clans_alliance_name.append(str(td_tag_content.find('a').contents[0]))
    else:
        all_of_clans_alliance_name.append('-')
    return all_of_clans_alliance_name


def get_clans_leader_name(td_tag_content, all_of_clans_leader_names):
    if td_tag_content.find('a') is not None:
        all_of_clans_leader_names.append(str(td_tag_content.find('a').contents[0]))
    else:
        all_of_clans_leader_names.append('неизвестен')
    return all_of_clans_leader_names


def get_clans_raiting_symbol(td_tag_content, all_of_clans_raiting_symbols):
    if td_tag_content.find('span').find(class_='dif-no') is not None:
        all_of_clans_raiting_symbols.append('  ')
    if td_tag_content.find('span').find(class_='dif-up') is not None:
        all_of_clans_raiting_symbols.append(str(td_tag_content.find('span').find(class_='dif-up').contents[0]))
    if td_tag_content.find('span').find(class_='dif-down') is not None:
        all_of_clans_raiting_symbols.append(str(td_tag_content.find('span').find(class_='dif-down').contents[0]))
    return all_of_clans_raiting_symbols


def get_top_50(top_50_clans_url):

    all_of_clans_position = [' ']
    all_of_clans_position_symbols = [' ']
    all_of_clans_names = ['клан']
    all_of_clans_id = []
    all_of_clans_count = ['численность']
    all_of_clans_alliance_names = ['альянс']
    all_of_clans_leader_names = ['лидер']
    all_of_clans_rating = ['рейтинг']
    all_of_clans_raiting_symbols = [' ']

    html_code = BeautifulSoup(get_html_code(top_50_clans_url), 'html.parser')
    tbody_html = html_code.find('tbody')
    clan_html_block = tbody_html.find_all('tr')

    for blocks in clan_html_block:
        tag_number = 1
        td_blocks = blocks.find_all('td')
        for td_tag_content in td_blocks:
            if tag_number == 1:

                all_of_clans_position = get_calns_position(td_tag_content,
                                                           all_of_clans_position
                                                           )
                get_clans_symbol_of_position(td_tag_content,
                                             all_of_clans_position_symbols
                                             )
            if tag_number == 2:

                clan_name = str(blocks.find('a').contents[0])
                all_of_clans_names.append(clan_name)

                clan_id = get_id(str(blocks.find('a')))
                all_of_clans_id.append(clan_id)

                clan_count = str(get_count_from_str(str(blocks.find(class_='add').contents[0])))
                all_of_clans_count.append(clan_count)

            if tag_number == 3:

                all_of_clans_alliance_names = get_clans_alliance(td_tag_content,
                                                                 all_of_clans_alliance_names
                                                                 )
            if tag_number == 4:

                all_of_clans_leader_names = get_clans_leader_name(td_tag_content,
                                                                  all_of_clans_leader_names
                                                                  )
            if tag_number == 5:

                clan_rating = str(td_tag_content.find('span').contents[0])
                all_of_clans_rating.append(clan_rating)

                all_of_clans_raiting_symbols = get_clans_raiting_symbol(td_tag_content,
                                                                        all_of_clans_raiting_symbols
                                                                        )
            tag_number += 1

    all_of_clans_information = [all_of_clans_position, all_of_clans_position_symbols,
                                all_of_clans_names, all_of_clans_id, all_of_clans_count,
                                all_of_clans_alliance_names, all_of_clans_leader_names,
                                all_of_clans_rating, all_of_clans_raiting_symbols
                                ]
    return all_of_clans_information


def get_header_info(html_code):
    all_clans_header_data = []
    header_title = []
    tr_tag = html_code.find(class_='values').find_all('tr')
    for number in range(len(tr_tag)):
        td_tag_content = tr_tag[number]
        title = str(td_tag_content.find('th').contents[0]) + ' '
        if td_tag_content.find('td') is not None:
            td_content = str(td_tag_content.find('td').contents[0])
        if td_tag_content.find('a') is not None:
            a_content = str(td_tag_content.find('a').contents[0])

        # GET WEB SITE #
        if str(get_name_of_th(tr_tag[number])) == 'Ссылка:':
            header_title.append(title)
            all_clans_header_data.append(a_content)

        # GET LEADER NAME #
        if str(get_name_of_th(tr_tag[number])) == 'Лидер:':
            header_title.append(title)
            all_clans_header_data.append(a_content)

        # GET STATS #
        if str(get_name_of_th(tr_tag[number])) == 'Персонажей:':
            header_title.append(title)
            all_clans_header_data.append(td_content + str(td_tag_content.find(class_='add').contents[0]))

        # GET PROF INFO #
        if str(get_name_of_th(tr_tag[number])) == 'Профессии:':
            header_title.append(title)
            all_clans_header_data.append(td_content)

        # GET TURNOVER INFO #
        if str(get_name_of_th(tr_tag[number])) == 'Текучка:':
            header_title.append(title)
            b_tag = td_tag_content.find_all('font')
            all_clans_header_data.append(
                td_content + b_tag[0].contents[0] + td_tag_content.find('td').contents[2] + b_tag[0].contents[0] +
                td_tag_content.find('td').contents[4])

        # GET ALLIANCE INFO #
        if str(get_name_of_th(tr_tag[number])) == 'Альянс:':
            header_title.append(title)
            all_clans_header_data.append(a_content)

        # GET HALL INFO #
        if str(get_name_of_th(tr_tag[number])) == 'Холл:':
            a_tag = td_tag_content.find_all('a')
            header_title.append(a_tag[0].contents[0] + ': ')
            all_clans_header_data.append(td_content + '(' + a_tag[1].contents[0] + ')')

        # GET CASTLE INFO #
        if str(get_name_of_th(tr_tag[number])) == 'Замок:':
            a_tag = td_tag_content.find_all('a')
            header_title.append(str(a_tag[0].contents[0]) + ': ')
            all_clans_header_data.append(str(a_tag[1].contents[0]) + ' (' + str(a_tag[2].contents[0]) + ')')

        # GET FORTRESS INFO #
        if str(get_name_of_th(tr_tag[number])) == 'Крепость:':
            header_title.append(str(td_tag_content.find('td').contents[0]))
            all_clans_header_data.append('(' + str(td_tag_content.find_all('a')[1].contents[0]) + ')')

        # GET ABOUT #
        if str(get_name_of_th(tr_tag[number])) == 'О клане:':
            string = str(td_tag_content.select('div')[0].get_text())
            new_string = string.split('\n')[1]
            header_title.append(title)
            if new_string == '':
                all_clans_header_data.append('Описание отсутствует')
            else:
                all_clans_header_data.append(string.split('\n')[1])

    return [header_title, all_clans_header_data]


def get_members_table(html_code):
    clan_member_name = ['Имя']
    clan_member_title = ['Титул']
    clan_member_class = ['Класс']
    clan_member_race = ['Раса']
    clan_member_lvl = ['Ур.']
    clan_member_up_date = ['Обновлен']
    tbody_tag = html_code.find(class_='tablesorter').find('tbody')
    tr_blocks = tbody_tag.find_all('tr')
    for tr_block_content in tr_blocks:
        td_blocks = tr_block_content.find_all('td')
        tag_number = 1
        for td_blocks_content in td_blocks:

            # GET MEMBER NAME #
            if tag_number == 1:
                member_name = td_blocks_content.find(class_='black').contents[0]
                clan_member_name.append(member_name)
                if is_title(td_blocks_content):
                    member_title = td_blocks_content.find(class_='add').contents[0]
                else:
                    member_title = ''
                clan_member_title.append(member_title)

            # GET MEMBER CLASS #
            if tag_number == 2:
                member_class = td_blocks_content.find('span').contents[0]
                clan_member_class.append(member_class)

            # GET MEMBER RACE #
            if tag_number == 3:
                member_race = td_blocks_content.find('font').contents[0]
                clan_member_race.append(member_race)

            # GET MEMBER LvL #
            if tag_number == 4:
                member_lv_l = td_blocks_content.contents[0]
                clan_member_lvl.append(str(member_lv_l) + str(td_blocks_content.find('span').contents[0]))

            # GET MEMBER UpDate #
            if tag_number == 5:
                member_up_date = td_blocks_content.find('span').contents[0]
                clan_member_up_date.append(member_up_date)

            tag_number += 1

    return [clan_member_name, clan_member_title, clan_member_class,
            clan_member_race, clan_member_lvl, clan_member_up_date]


def get_percentages(obj, count):
    ratio = []
    length = len(obj)
    total = 0
    for number in range(length):
        total += count[number]
    for number in range(length):
        number = int(count[number]) / int(total) * 100
        number = round(number, 2)
        ratio.append(str(number) + '%')
    return ratio


def get_clans_statistics(all_members_data):
    clan_member_race = all_members_data[3]
    clan_member_class = all_members_data[2]
    clan_member_lvl = all_members_data[4]
    races, race_counts = get_obj_info(clan_member_race)
    classes, class_counts = get_obj_info(clan_member_class)
    lvls, lvl_counts = get_obj_info(clan_member_lvl)
    races_ratio = get_percentages(races, race_counts)
    classes_ratio = get_percentages(classes, class_counts)
    lvls_ratio = get_percentages(lvls, lvl_counts)
    clan_statistics = [races, race_counts, races_ratio,
                       classes, class_counts,
                       classes_ratio, lvls,
                       lvl_counts, lvls_ratio]
    return clan_statistics


def get_server_stats(server_name):
    profession_name = [[], [], [], []]
    profession_count = [[], [], [], []]
    site_url = 'http://l2on.net/?c=userdata&a=inf&world' + str(server_name)
    html_code = BeautifulSoup(get_html_code(site_url), 'html.parser')
    table_tags = html_code.find(class_='content-userdata content-userdata-inf').find_all(class_='classes')
    table_number = 0
    for TableTag in table_tags:
        tr_tags = TableTag.find_all('tr')
        for trTag in tr_tags:
            profession = trTag.find('a').contents[0]
            count = trTag.find(class_='count').contents[0]
            profession_name[table_number].append(profession)
            profession_count[table_number].append(count)
        table_number += 1

    return profession_name, profession_count


def get_second_profession(first_prof, all_profession_names, all_profession_counts):
    classes = {'Воитель': ('Копейщик', 'Гладиатор'),
               'Рыцарь': ('Паладин', 'Мститель'),
               'Маг': ('Властитель Огня', 'Некромант', 'Колдун'),
               'Клерик': ('Епископ', 'Проповедник'),
               'Светлый Рыцарь': ('Рыцарь Евы', 'Менестрель'),
               'Разведчик': ('Следопыт', 'Серебряный Рейнджер'),
               'Светлый Маг': ('Певец Заклинаний', 'Последователь Стихий'),
               'Оракул Евы': ['Мудрец Евы'],
               'Темный Рыцарь': ('Рыцарь Шилен', 'Танцор Смерти'),
               'Ассасин': ('Странник Бездны', 'Призрачный Рейнджер'),
               'Темный Маг': ('Заклинатель Ветра', 'Последователь Тьмы'),
               'Оракул Шилен': ['Мудрец Шилен'],
               'Налетчик': ['Разрушитель'],
               'Монах': ['Отшельник'],
               'Шаман': ('Верховный Шаман', 'Вестник Войны'),
               'Собиратель': ['Охотник за Наградой'],
               'Ремесленник': ['Кузнец'],
               'Солдат': ('Берсерк', 'Палач'),
               'Надзиратель': ('Палач', 'Арбалетчик'),
               'Воин Артеи': ['Боец Сайхи'],
               'Маг Артеи': ['Последователь Сайхи']}
    first_prof_count = all_profession_counts[3][all_profession_names[3].index(first_prof)]
    professions = []
    count = []
    second_prof_list = all_profession_names[2]
    second_prof = classes[first_prof]
    for prof in range(len(second_prof)):
        position_in_list = second_prof_list.index(second_prof[prof])
        professions.append(second_prof[prof])
        count.append(all_profession_counts[2][position_in_list])
    return professions, count, first_prof_count


def calc_persentage(count):
    total = int(0)
    percentage = []
    for number in range(len(count)):
        total += int(count[number])
    for number in range(len(count)):
        calc = int(count[number]) / total
        percentage.append(round(calc * 100, 2))
    return percentage


def get_profession_stats(profession_name, profession_count):

    first_profession = []

    first_branch_of_the_second_profession = []
    second_branch_of_the_second_profession = []
    third_branch_of_the_second_profession = []

    percentages_of_first_branch = []
    percentages_of_second_branch = []
    percentages_of_third_branch = []

    first_class = ['Воитель', 'Рыцарь', 'Маг', 'Клерик', 'Светлый Рыцарь', 'Разведчик', 'Светлый Маг', 'Оракул Евы',
                   'Темный Рыцарь', 'Ассасин', 'Темный Маг', 'Оракул Шилен', 'Налетчик', 'Монах', 'Шаман', 'Собиратель',
                   'Ремесленник', 'Солдат', 'Надзиратель']

    for prof in first_class:
        professions, count, first_prof_count = get_second_profession(prof, profession_name, profession_count)
        per = calc_persentage(count)
        first_profession.append(prof)
        prof_length = len(count)
        first_profession.append(' ')
        first_profession.append(' ')

        first_prof_branch = ' '
        second_prof_branch = ' '
        third_prof_branch = ' '

        first_perc_branch = ' '
        second_perc_branch = ' '
        third_perc_branch = ' '

        if prof_length == 3:
            first_prof_branch = professions[0]
            first_perc_branch = str(per[0])+'%'
            second_prof_branch = professions[1]
            second_perc_branch = str(per[1])+'%'
            third_prof_branch = professions[2]
            third_perc_branch = str(per[2])+'%'

        if prof_length == 2:
            first_prof_branch = professions[0]
            first_perc_branch = str(per[0])+'%'
            second_prof_branch = professions[1]
            second_perc_branch = str(per[1])+'%'

        if prof_length == 1:
            first_prof_branch = professions[0]
            first_perc_branch = str(per[0])+'%'

        first_branch_of_the_second_profession.append(first_prof_branch)
        second_branch_of_the_second_profession.append(second_prof_branch)
        third_branch_of_the_second_profession.append(third_prof_branch)

        percentages_of_first_branch.append(first_perc_branch)
        percentages_of_second_branch.append(second_perc_branch)
        percentages_of_third_branch.append(third_perc_branch)

    second_profession = [first_branch_of_the_second_profession,
                         second_branch_of_the_second_profession,
                         third_branch_of_the_second_profession]

    percentages = [percentages_of_first_branch,
                   percentages_of_second_branch,
                   percentages_of_third_branch]

    return first_profession, second_profession, percentages
