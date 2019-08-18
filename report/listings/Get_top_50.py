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
