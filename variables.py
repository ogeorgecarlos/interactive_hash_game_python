# Lists used during the game
row_colum_combination = []
game_used = []
avatar_list = ['😜', '🤐', '😎', '👧']

# variables using during the game
player1 = ''
player2 = ''
player_now = ''
player_before = ''

# This is all possible combinations of victory in the hash
# if the same avatar is in the three positions of row/column
# the game is stoped and winner is show
vic1 = ((1, 1), (2, 2), (3, 3))
vic2 = ((1, 3), (2, 2), (3, 1))
vic3 = ((1, 1), (1, 2), (1, 3))
vic4 = ((2, 1), (2, 2), (2, 3))
vic5 = ((3, 1), (3, 2), (3, 3))
vic6 = ((1, 1), (2, 1), (3, 1))
vic7 = ((1, 2), (2, 2), (3, 2))
vic8 = ((1, 3), (2, 3), (3, 3))
