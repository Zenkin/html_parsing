
def print_server_pofession_stats(first_profession, second_profession, percentages):
    if IsOutputToConsole:
        for i in range(len(second_profession[0])):
            print(first_profession[i*3])
            print(second_profession[0][i].ljust(25) + ' '
                  + second_profession[1][i].ljust(25) + ' '
                  + second_profession[2][i].ljust(25)
                  )
            print(str(percentages[0][i]).ljust(25) + ' '
                  + str(percentages[1][i]).ljust(25) + ' '
                  + str(percentages[2][i]).ljust(25)
                  )
            print('')

