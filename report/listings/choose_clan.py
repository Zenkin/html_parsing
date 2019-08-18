
def choose_clan():
    print('')
    selected_clan_number = input('Choose clan( 1-50):'.rjust(30))
    if IsOutputToConsole:
        clear_screen()

    return int(selected_clan_number)

