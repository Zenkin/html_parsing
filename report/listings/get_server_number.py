
def get_server_number():
    clear_screen()

    print('#########   HELLO MY FRIEND   ##########'.center(100))
    print("######### LET's START PARSING ##########".center(100))
    print('Choose server: '.center(100))
    numb = 1
    for ServerName in ServersName:
        print(('(' + str(numb) + ')' + ServerName).center(100))
        numb += 1

    server_number = input('Server number _'.rjust(30))

    return int(server_number)

