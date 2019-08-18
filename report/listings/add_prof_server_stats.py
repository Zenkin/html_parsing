
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

