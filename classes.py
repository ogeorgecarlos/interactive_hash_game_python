from functions import user_name_validator

class Hash:
    def __init__(self):
        self.column = [' ', ' 1', ' 2', ' 3']
        self.row1 = [1, '⬜', '⬜', '⬜']
        self.row2 = [2, '⬜', '⬜', '⬜']
        self.row3 = [3, '⬜', '⬜', '⬜']
        self.hash_list = [self.column, self.row1, self.row2, self.row3]

# this class will build name and avatar for each player
class player:
    def __init__(self):
        self.nickname = user_name_validator()
        self.avatar = ""