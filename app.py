import gameboard
import player

print("Welcome to the game!")
print("Instructions: ")
print("To move up: w")
print("To move down: s")
print("To move left: a")
print("To move right: d")

print("Try to get to the end! Good Luck!")
print("-----------------------------")


board = gameboard.GameBoard()
# Create a new GameBoard called board
player = player.Player(3, 2)
# Create a new Player called player starting at position 3,2

while True:
    board.printBoard(player.rowPosition, player.columnPosition)
    selection = input("Make a move: ")
    # TODO
    # Move the player through the board
    if (selection =="w"):
        player.moveUp()
        board.checkMove(player.columnPosition, player.rowPosition -1)
       
    elif (selection =="s"):
        player.moveDown()
        board.checkMove(player.columnPosition, player.rowPosition +1)
        
    elif (selection =="a"):
        player.moveLeft()
        board.checkMove(player.rowPosition,  player.columnPosition -1)
        
    elif (selection =="d"):
        player.moveRight()
        board.checkMove(player.rowPosition,  player.columnPosition +1)
    
    if board.checkWin(player.rowPosition, player.columnPosition):  
       print("You Win")
       break
        
        
    # Check if the player has won, if so print a message and break the loop!
