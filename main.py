from os import system
from time import sleep

from classes import Hash, player
from functions import (choice_colum_row, header, integer_validator,
                       victory_checker)
from variables import (avatar_list, game_used, vic1, vic2, vic3, vic4, vic5,
                       vic6, vic7, vic8)

# --- MAIN PROGRAM ---
header('HASH GAME!🐱‍🏍')

# Its get the user's nickname and create the usera
player1 = player()
player2 = player()

print(f'\n🎉 Hey! Welcome to game {player1.nickname} and {player2.nickname}!')
#  Here will be chosen who will be the first to choose an avatar.
while True:
    print('Who will be the first to choose a avatar?\n')
    print(f'''
1 - {player1.nickname}
2 - {player2.nickname}
    \n''')
    choose = input('✅ Enter index or nickname: ').strip().capitalize()

    # conditional's to validate the choose
    if choose == '1' or choose == player1.nickname:
        print(f'\n✅ Great, {player1.nickname}! Witch your prefered avatar?\n')
        # here we starts to use the variable "player_now and _before"
        # the porpose is to define who is the time's player
        player_now = player1
        player_before = player2
        break
    elif choose == '2' or choose == player2:
        print(f'\n✅ Great, {player2.nickname}! Witch your prefered avatar?\n')
        player_now = player2
        player_before = player1
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

# Now we show a avatar's list to choose from
count = 1
while True:
    for ind, avatar in enumerate(avatar_list):
        print(ind, '-', avatar)
    choose = integer_validator("\n✅ Enter the number list of your Avatar: ")

    # conditional's to validate the choose of avatar
    if choose not in range(0, len(avatar_list)):
        print("\n😐 \033[31mIt's not a valid option. Try again!\033[m")
        sleep(2)
        system('cls')
    elif count == 1:
        # now we merge the chosse in the player class
        player_now.avatar = avatar_list[choose]
        # now we know that the first already played,...
        # and the next will be the player_before
        count += 1
        # and erase the chosen avatar from list
        # that will be show for player_before
        del avatar_list[choose]
        print(
            f"\n✅ Hey, {player_before.nickname}! It's your time? Witch your \
                prefered avatar?\n")
    elif count == 2:  # player2's time
        player_before.avatar = avatar_list[choose]
        break
system('cls')

# --- The game ---
header('THE BIG CHALLENGE! 🔥')
print(f'''
      {player1.nickname} {player1.avatar} ❌ {player2.avatar} {player2.nickname}
''')

# the players will choose who the first to start's to play
print('Who will be the first to play?\n')
print(f'''
1 - {player1.nickname}
2 - {player2.nickname}
    \n''')

# This conditional will validate the player's choose
while True:
    choose = input('✅ Enter index or nickname: ').strip().capitalize()
    # Conditionals to validate the choose
    if choose == '1' or choose == player1.nickname:
        print(
            f'\n✅ Great, {player1.nickname}! Now choice the row and column \
                to mark: \n')
        player_now = player1
        player_before = player2
    elif choose == '2' or choose == player2.nickname:
        print(f'\n✅ Great, {player2.nickname}! choice the row and column \
            to mark:\n')
        player_now = player2
        player_before = player1
        break
    else:
        print("\n😐 \033[31mIt's not a valid option. Try again!\033[m")

# Here we presents the hash and starts the game
hash_game = Hash()
while True:
    for item in hash_game.hash_list:
        print(8*' ', end='')
        print(*item)
    print()

    column = choice_colum_row('Column')
    row = choice_colum_row('Row')

    # here we will check if the last combination choosen is not used before
    row_colum_combination = (row, column)
    if row_colum_combination not in game_used:
        game_used.append(row_colum_combination)
    else:
        print(f"{player_now.nickname}, you can't repeat a choice. Try again")
        continue

    # And to atribute the player's avatar to your choosen in the hash
    hash_game.hash_list[row][column] = player_now.avatar

    # here we trade the position player to move on in the game
    other_player = player_now
    player_now = player_before
    player_before = other_player

    victory_checker(game_used, vic1, hash_game, player1, player2)
    victory_checker(game_used, vic2, hash_game, player1, player2)
    victory_checker(game_used, vic3, hash_game, player1, player2)
    victory_checker(game_used, vic4, hash_game, player1, player2)
    victory_checker(game_used, vic5, hash_game, player1, player2)
    victory_checker(game_used, vic6, hash_game, player1, player2)
    victory_checker(game_used, vic7, hash_game, player1, player2)
    victory_checker(game_used, vic8, hash_game, player1, player2)
    system('cls')

    print(f"{player_now.nickname} it's your time!\n")
