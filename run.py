from random import randint


class Missions:
    """
        Sets up the mission choosen to be played by the player.
        """

    def __init__(self, board_size, torpedoes, fleet, name):
        self.board_size = board_size
        self.torpedoes = torpedoes
        self.fleet = fleet
        self.name = name

        player_board = [
            ['o'] * self.board_size for x in range(self.board_size)]
        board = create_board(self.board_size)
        print('Note: TOP LEFT HAND  "o" is ROW 0, COLUMN 0')
        print(f"Player's guess: {player_board}")
        ship_grid = position_ships(board, self.board_size)
        print()
        print(f'playing board with ships: {ship_grid}')
        print()
        battleships = 0
        play_on = False
        while play_on is False:
            guess = get_guess(self.board_size, player_board)
            battleships = update_board(
                guess, player_board, ship_grid, battleships)
            print()
            print(f'You have sunk {battleships} battleships.\n')
            self.torpedoes -= 1
            print(f'You have {self.torpedoes} torpedo(es) left.\n')
            if self.torpedoes == 0 or battleships == self.fleet:
                print('!!! Mission Over !!!')
                play_on = True
                if self.torpedoes == 0 or battleships != self.fleet:
                    print('Enemy ships have evaded your tropedoes!')
                    print(f'Better luck next time Admiral {self.name}!')
                else:
                    if battleships == self.fleet:
                        print(f'"Well done Admrial {self.name}')
                        print('You have destroyed the enemies fleet!')
            else:
                print('Launch another torpedo?')
                print('Press any key to continue or n to exit.')
                ans = input()
                print()
                if ans == 'n' or ans == 'N':
                    play_on = True
                    print(
                        f"Mission aborted, Admiral {self.name}'s orders.\n \n")


def create_board(data):
    """
   To set up the grid on which the game will be palyed.
    """
    grid = [['o'] * data for x in range(data)]
    for r in grid:
        for c in r:
            print(c, end=" ")
        print()
    return grid


def position_ships(grid, size):
    """
    To determin the row and column positions of the battleships.
    """
    board = grid
    for x in range(size):
        y = randint(0, size - 1)
        board[x][y] = 'S'
    return board


def get_guess(size, grid):
    """
    To get row and colum positon from the player, where torpedoes
    are to be launched onto the board.
    """
    duplicate = True
    while duplicate is True:
        location = []
        row = input(f'Enter a row number from 0 to {size - 1}.\n')
        row = validate_guess(row, size)
        location.append(row)
        col = input(f'Enter a column value from 0 to {size - 1}.\n')
        col = validate_guess(col, size)
        location.append(col)
        duplicate = duplicate_check(location, grid)
    return location


def validate_guess(num, size):
    """
    To check the values entered are intergers, that
    values do not exceed the size of the board.
    """
    ok = False
    while ok is False:
        try:
            num = int(num)
            if int(num) < 0 or int(num) > size-1:
                raise ValueError
            else:
                ok = True
        except ValueError:
            print(f'Your input must be a whole number from 0 to {size-1}.')
            num = input('Type in a number:\n')
    return int(num)


def duplicate_check(check, grid):
    """
    To check for duplicate guesses and request new guess if there
    duplicate is given.
    """
    num1 = check[0]
    num2 = check[1]
    if grid[num1][num2] == 'X' or grid[num1][num2] == 'S':
        print(f'Current guess {check} is a duplicate\n')
        print('Re-enter your guess.\n')
        duplicate = True
    else:
        duplicate = False
    return duplicate


def update_board(data, player, ships, sunk_ships):
    """
    Takes players guess, updates and prints the current playing board.
    """
    row = data[0]
    col = data[1]
    if ships[row][col] == 'S':
        print(f'Congratulations, your {data} launch has resulted in a Hit!')
        player[row][col] = 'S'
        sunk_ships += 1
    else:
        print(f'Your {data} guess resulted in a miss.')
        player[row][col] = 'X'
    for r in player:
        for c in r:
            print(c, end=" ")
        print()
    return sunk_ships


def play_game():
    """
    Explains Sets up the rules of the game and allows
    the player to choose the game level they want to play. 
    """
    print(f"Welcome to My Battleship Admiral {name}.\n")
    print('Your mission:')
    print("To locate and destroy all of the enemies' ")
    print('battleships, BEFORE your torpedoes RUN OUT.\n')
    print('*' * 50)
    print('There are 3 missions to choose from,')
    print('the higher the number, the greater the skill')
    print('needed to complete your task.')
    print('*' * 50)
    print('Mission 0: Is a 3 x 3 grid, with 3 enemy ships,')
    print('that must be destroyed with 6 torpeodoes.')
    print()
    print('Mission 1: Is a 4 x 4 grid, with 4 enemy ships,')
    print('that must be destroyed with 11 torpeodoes.')
    print()
    print('Mission 2: Is a 5 x 5 grid, with 5 enemy ships,')
    print('that must be destroyed with 17 torpeodoes.')
    print('*' * 50)
    max = 3
    mission_level = input(
        f'Select your mission number, Admiral {name} \n')
    game = validate_guess(mission_level, max)
    if game == 0:
        Missions(3, 6, 3, name)
    elif game == 1:
        Missions(4, 11, 4, name)
    else:
        Missions(5, 17, 5, name)


name = input('Enter your name: ')

play_again = True
while play_again is True:
    play_game()
    check = False
    print('Would you like to take on another mission?\n')
    while check is False:
        answer = input('Enter y for yes and n for no.\n')
        if answer in ('y', 'Y', 'n', 'N'):
            check = True
    if answer in ('n', 'N'):
        play_again = False
print(f'Thank you for your service Admiral {name}!')
