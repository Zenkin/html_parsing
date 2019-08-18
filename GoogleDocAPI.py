import gspread
import oauth2client.service_account

scope = ['https://spreadsheets.google.com/feeds']
creds = oauth2client.service_account.ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)


def add_to_google_sheet(sheet_name, worksheet_name, data_list, start_column, row_offset=0, column_offset=0):
    list_length = len(data_list)
    sheet_data = client.open(sheet_name).worksheet(worksheet_name)
    for row in range(list_length):
        sheet_data.update_cell(row + 1 + row_offset, start_column + column_offset, data_list[row])


def add_prof_server_stats(first_profession, second_profession, percentages):
    sheet_name = 'l2onParsing'
    worksheet_name = 'ProfServerStats'
    sheet_data = client.open(sheet_name).worksheet(worksheet_name)
    list_length = len(first_profession)
    for row in range(list_length):
        sheet_data.update_cell(row + 1, 1, first_profession[row])
    row = 1
    for i in range(len(second_profession[0])):
        column = 2
        for j in range(3):
            sheet_data.update_cell(row, column, second_profession[j][i])
            column += 1
        row += 3
    row = 2
    for i in range(len(percentages[0])):
        column = 2
        for j in range(3):
            sheet_data.update_cell(row, column, percentages[j][i])
            column += 1
        row += 3


def clear_sheet(sheet_name):
    sheet_data = client.open(sheet_name).sheet1
    sheet_data.clear()


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
