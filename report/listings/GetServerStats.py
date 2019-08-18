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
