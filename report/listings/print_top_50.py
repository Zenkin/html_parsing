
def print_top_50(top_50_clans_information, server_number):
    if IsOutputToConsole:
        print(('############# Top 50 clans of ' + ServersName[int(server_number) - 1] + ' #############').center(100))
        for i in range(51):
            print(top_50_clans_information[0][i].center(4), top_50_clans_information[1][i].rjust(4),
                  top_50_clans_information[2][i].ljust(15), top_50_clans_information[4][i].center(15),
                  top_50_clans_information[5][i].ljust(20), top_50_clans_information[6][i].ljust(20),
                  top_50_clans_information[7][i].ljust(5), top_50_clans_information[8][i])

