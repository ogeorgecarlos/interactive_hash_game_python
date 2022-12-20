from os import system
from time import sleep
import sys


# Lista with emoji thats build a figure
# and will be replaced during the game
class Hash:
    def __init__(self):
        self.column = [' ', ' 1', ' 2', ' 3']
        self.row1 = [1, '⬜', '⬜', '⬜']
        self.row2 = [2, '⬜', '⬜', '⬜']
        self.row3 = [3, '⬜', '⬜', '⬜']
        self.hash_list = [self.column, self.row1, self.row2, self.row3]

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


# this class will build name and avatar for each player
class player:
    def __init__(self):
        self.nickname = user_name_validator()
        self.avatar = ""


def victory_checker(game_used, vic, hash_game, user1, user2):
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


row_colum_combination = []
game_used = []


header('HASH GAME!🐱‍🏍')

# Its get the user's nickname and create the usera
user1 = player()
user2 = player()

print(f'\n🎉 Hey! Welcome to game {user1.nickname} and {user2.nickname}!')

# Now the users will choose their's avatar
avatar_list = ['😜', '🤐', '😎', '👧']
while True:
    print('Who will be the first to choose a avatar?\n')
    print(f'''
1 - {user1.nickname}
2 - {user2.nickname}
    \n''')
    choose = input('✅ Enter index or nickname: ').strip().capitalize()

    if choose == '1' or choose == user1.nickname:
        print(f'\n✅ Great, {user1.nickname}! Witch your prefered avatar?\n')
        player_now = user1
        player_before = user2
        break
    elif choose == '2' or choose == user2:
        print(f'\n✅ Great, {user2.nickname}! Witch your prefered avatar?\n')
        player_now = user2
        player_before = user1
        break
    elif choose == '':
        print("\n🤷‍♂️ You might to enter one player.. let's try again...")
        sleep(2)
        system('cls')
    else:
        print("\n🤐 hmm...I dont find this option.")
        print("Enter with a avalaible option.")
        print("\nLet's try again...")
        sleep(2)
        system('cls')

count = 1
while True:
    for ind, avatar in enumerate(avatar_list):
        print(ind, '-', avatar)

    choose = integer_validator("\n✅ Enter the number list of your Avatar: ")

    if choose not in range(0, len(avatar_list)-1):
        print("\n😐 \033[31mIt's not a valid option. Try again!\033[m")
        sleep(2)
        system('cls')
    elif count == 1:
        player_now.avatar = avatar_list[choose]
        count += 1
        del avatar_list[choose]
        print(
            f"\n✅ Hey, {player_before.nickname}! It's your time? Witch your prefered avatar?\n")
    elif count == 2:
        player_before.avatar = avatar_list[choose]
        break

system('cls')

header('THE BIG CHALLENGE! 🔥')
print(f'''
      {user1.nickname} {user1.avatar} ❌ {user2.avatar} {user2.nickname}
''')

print('Who will be the first to play?\n')
print(f'''
1 - {user1.nickname}
2 - {user2.nickname}
    \n''')
choose = input('✅ Enter index or nickname: ').strip().capitalize()

if choose == '1' or choose == user1.nickname:
    print(
        f'\n✅ Great, {user1.nickname}! Now choice the row and column to mark: \n')
    player_now = user1
    player_before = user2
elif choose == '2' or choose == user2:
    print(f'\n✅ Great, {user2.nickname}! choice the row and column to mark:\n')
    player_now = user2
    player_before = user1
else:
    print("\n😐 \033[31mIt's not a valid option. Try again!\033[m")

hash_game = Hash()
while True:
    for item in hash_game.hash_list:
        print(8*' ', end='')
        print(*item)
    print()

    while True:
        column = integer_validator("\n✅ Column: ")
        if column not in range(1, 4):
            print("Doesn't exist this column, try again..")
        else:
            break

    while True:
        row = integer_validator("\n✅ Row: ")
        if row not in range(1, 4):
            print("Doesn't exist this Row, try again..")
        else:
            break

    row_colum_combination = (row, column)
    if row_colum_combination not in game_used:
        game_used.append(row_colum_combination)
    else:
        print(f"{player_now.nickname}, you can't repeat a choice. Try again")
        continue

    hash_game.hash_list[row][column] = player_now.avatar

    # here we trade the position player to move onp
    other_player = player_now
    player_now = player_before
    player_before = other_player

    vic1 = ((1, 1), (2, 2), (3, 3))
    vic2 = ((1, 3), (2, 2), (3, 1))
    vic3 = ((1, 1), (1, 2), (1, 3))
    vic4 = ((2, 1), (2, 2), (2, 3))
    vic5 = ((3, 1), (3, 2), (3, 3))

    victory_checker(game_used, vic1, hash_game, user1, user2)
    victory_checker(game_used, vic2, hash_game, user1, user2)
    victory_checker(game_used, vic3, hash_game, user1, user2)
    victory_checker(game_used, vic4, hash_game, user1, user2)
    system('cls')

    print(f"{player_now.nickname} it's your time!")

    # victories possibles
    # first number in tuple is the row, second is the column
