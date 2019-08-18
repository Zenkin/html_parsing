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
