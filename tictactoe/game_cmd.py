def check_winner(board, player):
    '''check if the given player has won'''
    # check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
        
    # check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
        
    # diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True

    return False

move_count = 0

list_of_lists = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

dotted_line = "---------"

position_coordinates = {
    1:(0,0), 2:(0,1), 3:(0,2),
    4:(1,0), 5:(1,1), 6:(1,2),
    7:(2,0), 8:(2,1), 9:(2,2),
}

current_player = "X"

while True:
    print(f"Current Player: {current_player}")
    try:
        user_input = int(input("Enter a position (1-9): "))
    except ValueError:
        print("Please enter a valid number.")
        continue
    
    if user_input not in position_coordinates:
        print("Invalid position! Choose from 1 to 9.")
        continue
    
    row,col = position_coordinates[user_input]

    if list_of_lists[row][col] != " ":
        print("That position is already taken. Try another.")
        continue
    
    #valid move
    list_of_lists[row][col] = current_player
    move_count += 1

    #print the board
    for i in range(len(list_of_lists)):
        row_print = list_of_lists[i]
        print(f"{row_print[0]} | {row_print[1]} | {row_print[2]}")
        if i < len(list_of_lists)-1:
            print(dotted_line)

    # check for winner (after 5th move at minimum)
    if move_count >= 5 and check_winner(list_of_lists, current_player):
        print(f"Player {current_player} wins!")
        break
    
    # check for draw
    if move_count == 9:
        print("It's a draw. Game over!")
        break
    
    # switch turns *after* a successful move
    current_player = "O" if current_player == "X" else "X"
