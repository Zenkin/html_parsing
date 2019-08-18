
def load_all_data_in_google_doc(clan_header, all_member_data,
                                races_data, classes_data,
                                clan_lvl_data, first_profession_data,
                                second_profession_data, third_profession_data,
                                fourth_profession_data, first_profession,
                                second_profession, percentages):
    for list_count in range(len(clan_header)):
        sheet_name = 'l2onParsing'
        worksheet_name = 'ClanStats'
        add_to_google_sheet(sheet_name, worksheet_name, clan_header[list_count], list_count + 1)

    for list_count in range(len(all_member_data)):
        row_offset = 12
        sheet_name = 'l2onParsing'
        worksheet_name = 'ClanStats'
        add_to_google_sheet(sheet_name, worksheet_name, all_member_data[list_count],
                            list_count + 1, row_offset)

    for list_count in range(len(races_data)):
        sheet_name = 'l2onParsing'
        worksheet_name = 'ClanMemberStats'
        start_row = list_count + 1
        add_to_google_sheet(sheet_name, worksheet_name, races_data[list_count], start_row)

    for list_count in range(len(classes_data)):
        sheet_name = 'l2onParsing'
        worksheet_name = 'ClanMemberStats'
        start_row = list_count + 1
        row_offset = 0
        column_offset = 4
        add_to_google_sheet(sheet_name, worksheet_name, classes_data[list_count],
                            start_row, row_offset, column_offset)

    for list_count in range(len(clan_lvl_data)):
        sheet_name = 'l2onParsing'
        worksheet_name = 'ClanMemberStats'
        start_row = list_count + 1
        row_offset = 0
        column_offset = 8
        add_to_google_sheet(sheet_name, worksheet_name, clan_lvl_data[list_count],
                            start_row, row_offset, column_offset)

    for list_count in range(len(first_profession_data)):
        sheet_name = 'l2onParsing'
        worksheet_name = 'ServerStats'
        start_row = list_count + 1
        row_offset = 1
        column_offset = 0
        add_to_google_sheet(sheet_name, worksheet_name, first_profession_data[list_count],
                            start_row, row_offset, column_offset)

    for list_count in range(len(second_profession_data)):
        sheet_name = 'l2onParsing'
        worksheet_name = 'ServerStats'
        start_row = list_count + 1
        row_offset = 1
        column_offset = 3
        add_to_google_sheet(sheet_name, worksheet_name, second_profession_data[list_count],
                            start_row, row_offset, column_offset)

    for list_count in range(len(third_profession_data)):
        sheet_name = 'l2onParsing'
        worksheet_name = 'ServerStats'
        start_row = list_count + 1
        row_offset = 1
        column_offset = 6
        add_to_google_sheet(sheet_name, worksheet_name, third_profession_data[list_count],
                            start_row, row_offset, column_offset)

    for list_count in range(len(fourth_profession_data)):
        sheet_name = 'l2onParsing'
        worksheet_name = 'ServerStats'
        start_row = list_count + 1
        row_offset = 1
        column_offset = 9
        add_to_google_sheet(sheet_name, worksheet_name, fourth_profession_data[list_count],
                            start_row, row_offset, column_offset)

    add_prof_server_stats(first_profession, second_profession, percentages)

