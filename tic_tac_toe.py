from IPython.display import clear_output
import random
#1 function for displaying board
def display_board(b):
    clear_output()
    print(b[1]+'|'+b[2]+'|'+b[3])
    print(b[4]+'|'+b[5]+'|'+b[6])
    print(b[7]+'|'+b[8]+'|'+b[9])
    
#2 function that take user input and assign their markers
def player_input():
    marker = ''
    while marker !='X' and marker!= 'O':
        marker = input("Player 1 Choose X or O : ").upper()
    #return (player 1 marker , player 2 marker)      
    if marker == 'X':
        return ('X','O')    
    else:
        return ('O','X')

#3 func to place marker on desired position on board
def place_marker(board, marker, position):
    board[position] = marker
 
#4 func for checking if any player won
def win_check(b, m):
#return bool true or false
    return ((b[1] == m and b[2] == m and b[3] == m) or #row
            (b[4] == m and b[5] == m and b[6] == m) or #row
            (b[7] == m and b[8] == m and b[9] == m) or #row  
            (b[1] == m and b[4] == m and b[7] == m) or #column
            (b[2] == m and b[5] == m and b[8] == m) or #column
            (b[3] == m and b[6] == m and b[9] == m) or #column
            (b[1] == m and b[5] == m and b[9] == m) or #diagonal
            (b[3] == m and b[5] == m and b[7] == m))  #diagonal

#5 func to choose which player will go first and return name
def choose_first():
    flip = random.randint(0,1)
    if flip ==0:
        return 'Player 1'
    else:
        return 'Player 2' 
    
#6 func to check whether a space on the board is free or not and returns true or false
def space_check(board, position):
    return board[position] == ' '

#7 func to check full board or not
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

#8 func 
def player_choice(board, turn):
    position = 0
    while (position not in [1,2,3,4,5,6,7,8,9]) or (not space_check(board, position)) :
        position = int(input(turn + ' Choose a position 1-9 : '))
    return position    

#9 func for asking for play again or not and return true if want to play again
def replay():
    choice = input('Do you want to play again ? Enter YES or NO : ').upper()
    return choice == 'YES'

#10  final 
print("Welcome")
#while loop to continue running the game
while True:
    #play the game
    the_board = [' ']*10
    player1_marker,player2_marker = player_input()  #2 return 'X' and 'O' or 'O' and 'X'
    turn = choose_first()   #5 return player 1 or player 2
    print( turn + " will go first ")
    play_game = input("Ready to play ? YES or NO : ").upper()
    if play_game == 'YES' :
        game_on = True
    else:
        game_on = False
    # game play 
    while game_on : 
        if turn == 'Player 1' :
            # show board
            display_board(the_board)
            #choose a position 
            position = player_choice(the_board, turn) #8 return position choosen
            #place marker on position
            place_marker(the_board , player1_marker , position)  #3
            #check if won
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('PLAYER 1 WON')
                game_on =False
            else:
                #check for tie
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE GAME') 
                    game_on = False
                #no tie no win the next turn  
                else:
                    turn = 'Player 2'
           
        else:
            # show board
            display_board(the_board)
            #choose a position 
            position = player_choice(the_board, turn) #8 return position choosen
            #place marker on position
            place_marker(the_board , player2_marker , position)  #3
            #check if won
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('PLAYER 2 WON')
                game_on =False
            else:
                #check for tie
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE GAME') 
                    game_on = False
                #no tie no win the next turn  
                else:
                    turn = 'Player 1'
    if not replay():
        break






    
#test_board = ['#','X','O','X','O','X','O','X','O','X']
#display_board(test_board)
#player1_marker , player2_marker = player_input()
#place_marker(test_board,'@',4)
#display_board(test_board)
#print(win_check(test_board,'X'))
