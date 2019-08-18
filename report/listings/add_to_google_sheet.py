
def add_to_google_sheet(sheet_name, worksheet_name, data_list, start_column, row_offset=0, column_offset=0):
    list_length = len(data_list)
    sheet_data = client.open(sheet_name).worksheet(worksheet_name)
    for row in range(list_length):
        sheet_data.update_cell(row + 1 + row_offset, start_column + column_offset, data_list[row])

