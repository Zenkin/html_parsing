
def get_clan_info(clan_id):
    html_code = BeautifulSoup(get_html_code('http://l2on.net/?c=userdata&a=pledge&id=' + clan_id), 'html.parser')
    clan_header_titles, clan_header_all_data = get_header_info(html_code)
    all_members_data = get_members_table(html_code)

    return clan_header_titles, clan_header_all_data, all_members_data

