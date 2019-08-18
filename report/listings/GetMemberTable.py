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

            if tag_number == 1:
                member_name = td_blocks_content.find(class_='black').contents[0]
                clan_member_name.append(member_name)
                if is_title(td_blocks_content):
                    member_title = td_blocks_content.find(class_='add').contents[0]
                else:
                    member_title = ''
                clan_member_title.append(member_title)

            if tag_number == 2:
                member_class = td_blocks_content.find('span').contents[0]
                clan_member_class.append(member_class)

            if tag_number == 3:
                member_race = td_blocks_content.find('font').contents[0]
                clan_member_race.append(member_race)

            if tag_number == 4:
                member_lv_l = td_blocks_content.contents[0]
                clan_member_lvl.append(str(member_lv_l) + str(td_blocks_content.find('span').contents[0]))

            if tag_number == 5:
                member_up_date = td_blocks_content.find('span').contents[0]
                clan_member_up_date.append(member_up_date)

            tag_number += 1

    return [clan_member_name, clan_member_title, clan_member_class,
            clan_member_race, clan_member_lvl, clan_member_up_date]
