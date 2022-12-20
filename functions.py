
# this function create a header pattern during the game
def header(text):
    print(35*'-')
    print(f'{text:^35}')
    print(35*'-')
    print()


# this function check and valid the nickname
def user_name_validator():
    while True:
        user = input("✅ Whitch the player's one name?\n").strip()
        if user == '':
            print('❌\033[31m Enter with a valid nickname \033[m.\n')
        else:
            break
    return user.capitalize()


def integer_validator(text):
    while True:
        x = input(f'{text}')
        if x.isnumeric():
            break
        else:
            print("\n\033[31mIt's not a valid option. Try again..\033[m")
    return int(x)


def choice_colum_row(text):
    while True:
        x = integer_validator(f"\n✅ {text}: ")
        if x not in range(1, 4):
            print(f"Doesn't exist this {text}, try again..")
        else:
            break
    return int(x)


def victory_checker(game_used, vic, hash_game, user1, user2):
    import sys
    from time import sleep
    count = 0
    for item in game_used:
        if item in vic:
            count += 1
            if count == 3:
                list_conference = []
                for item in vic:
                    list_conference.append(
                        hash_game.hash_list[item[0]][item[1]])
                if list_conference[0] == list_conference[1] == list_conference[2]:
                    if list_conference[0] == user1.avatar:
                        print()
                        header(
                            f'{user1.avatar} {user1.nickname} é o vencedor!!')
                        sleep(5)
                        sys.exit()
                    else:
                        print()
                        header(
                            f'{user2.avatar} {user2.nickname} é o vencedor!!')
                        sleep(5)
                        sys.exit()
