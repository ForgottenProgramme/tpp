the_board= {
    'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
    'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
    'low-L': ' ', 'low-M': ' ', 'low-R': ' '
}

def print_board(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

print_board(the_board)

turn = 'X'
for i in range(9):
    print(f"It's {turn}'s turn. Which space to move to?")
    move=input()
    the_board[move]=turn
    print_board(the_board)
    
    if turn=='X':
        turn='O'
    else:
        turn='X'