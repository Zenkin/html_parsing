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

        if str(get_name_of_th(tr_tag[number])) == 'Ссылка:':
            header_title.append(title)
            all_clans_header_data.append(a_content)

        if str(get_name_of_th(tr_tag[number])) == 'Лидер:':
            header_title.append(title)
            all_clans_header_data.append(a_content)

        if str(get_name_of_th(tr_tag[number])) == 'Персонажей:':
            header_title.append(title)
            all_clans_header_data.append(td_content + str(td_tag_content.find(class_='add').contents[0]))

        if str(get_name_of_th(tr_tag[number])) == 'Профессии:':
            header_title.append(title)
            all_clans_header_data.append(td_content)

        if str(get_name_of_th(tr_tag[number])) == 'Текучка:':
            header_title.append(title)
            b_tag = td_tag_content.find_all('font')
            all_clans_header_data.append(
                td_content + b_tag[0].contents[0] + td_tag_content.find('td').contents[2] + b_tag[0].contents[0] +
                td_tag_content.find('td').contents[4])

        if str(get_name_of_th(tr_tag[number])) == 'Альянс:':
            header_title.append(title)
            all_clans_header_data.append(a_content)

        if str(get_name_of_th(tr_tag[number])) == 'Холл:':
            a_tag = td_tag_content.find_all('a')
            header_title.append(a_tag[0].contents[0] + ': ')
            all_clans_header_data.append(td_content + '(' + a_tag[1].contents[0] + ')')

        if str(get_name_of_th(tr_tag[number])) == 'Замок:':
            a_tag = td_tag_content.find_all('a')
            header_title.append(str(a_tag[0].contents[0]) + ': ')
            all_clans_header_data.append(str(a_tag[1].contents[0]) + ' (' + str(a_tag[2].contents[0]) + ')')

        if str(get_name_of_th(tr_tag[number])) == 'Крепость:':
            header_title.append(str(td_tag_content.find('td').contents[0]))
            all_clans_header_data.append('(' + str(td_tag_content.find_all('a')[1].contents[0]) + ')')

        if str(get_name_of_th(tr_tag[number])) == 'О клане:':
            string = str(td_tag_content.select('div')[0].get_text())
            new_string = string.split('\n')[1]
            header_title.append(title)
            if new_string == '':
                all_clans_header_data.append('Описание отсутствует')
            else:
                all_clans_header_data.append(string.split('\n')[1])

    return [header_title, all_clans_header_data]
