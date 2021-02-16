from grid import Grid

class TicTacToe:
    def __init__(self):
        self.grid = Grid()
        self.turn = "X"             # Start with X's turn
        self.toContinue = True      # Boolean variable to signify whether or not game can proceed
        self.winner = None

    # Main game play function:
    def play(self):
        while self.toContinue is True:
            # Display all the avaliable moves, the grid, current turn
            self.grid.show_positions()
            self.grid.show_grid()
            self.show_turn()

            # Current player chooses a position and makes a move - board is updated:
            pos = self.pick_position()
            valid = self.grid.move(pos, self.turn)
            while valid is False:
                print('That spot is already taken, please try again.')
                pos = self.pick_position()
                valid = self.grid.move(pos, self.turn)

            # Check if there are more moves to be made:
            self.toContinue = self.grid.are_moves_left()

            # Check if there is a winner after the last move was made:
            self.winner = self.grid.check_win()
            if self.winner != None:
                self.toContinue = False

            # Update the next turn
            self.update_turn()
            
        # Display final grid and result of the game    
        self.grid.show_grid()
        self.show_result()
        
        
    # Setter method to set the turn:
    def set_turn(self, turn):
        self.turn = turn

    # Getter method to get turn:
    def get_turn(self):
        return self.turn

    # Getter method to get winner:
    def get_winner(self):
        return self.winner

    # Helper method to display the current turn (player 1 or 2 / X or O):
    def show_turn(self):
        if self.turn == "X":
            print("X's Turn")
        else:
            print("O's Turn")

    # Helper method to update the current turn:
    def update_turn(self):
        if self.turn == "X":
            self.turn = "O"    # if current turn is X --> change to O
        elif self.turn == "O":
            self.turn = "X"    # if current turn is O --> change to X

    # Helper method to display the outcome of the game:
    def show_result(self):
        if self.winner is not None:
            print(self.winner + " wins!")
        else:
            print("It's a tie! - No moves left.")

    # Helper method to capture user's input - which position they are choosing
    # Returns pos choice as an integer.
    def pick_position(self):
        pos = input("Enter a position (1-9): ")
        while not pos.isdigit() or int(pos) > 9 or int(pos) < 1:
            pos = input("Invalid choice. Please select a number between 1 and 9: ")
        pos = int(pos) # convert to integer 
        return pos