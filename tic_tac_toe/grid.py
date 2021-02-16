class Grid:
    def __init__(self):
        self.grid = {   1: " ", 2: " ", 3: " ",
                        4: " ", 5: " ", 6: " ",
                        7: " ", 8: " ", 9: " " }
    
    # Displays the number positions on the grid:
    def show_positions(self):
        print("1 | 2 | 3")
        print("--+---+--")
        print("4 | 5 | 6")
        print("--+---+--")
        print("7 | 8 | 9 \n")

    # Displays the grid and its contents in its current state:
    def show_grid(self):
        print(self.grid[1] + " | " + self.grid[2] + " | " + self.grid[3])
        print("--+---+--")
        print(self.grid[4] + " | " + self.grid[5] + " | " + self.grid[6])
        print("--+---+--")
        print(self.grid[7] + " | " + self.grid[8] + " | " + self.grid[9] + "\n")

    # Getter method to get the internal instance variable - returns a dictionary
    def get_grid(self):
        return self.grid

    # Updates the grid with a new move
    # @position: 1-9 location on the grid
    # @player: X or O
    # Returns True if move successful, False if invalid.
    def move(self, position, player):
        if self.grid[position] == " ":
            self.grid[position] = player
            return True
        else: 
            return False

    # Checks if there are moves left to make
    # Returns true if yes, false if no.
    def are_moves_left(self):
        for i in range(1, 10):
            if self.grid[i] == " ":
                return True
        return False

    # Checks if there's a win on the grid:
    # Returns the character of the winning player if there's a win,
    # otherwise returns 'None' if no win
    def check_win(self):
        # Check horizontal:
        for i in range(1, 10, +3):
            if self.grid[i] != " " and self.grid[i] == self.grid[i+1] == self.grid[i+2]:
                return self.grid[i]
        
        # Check vertical:
        for i in range(1, 4):
            if self.grid[i] != " " and self.grid[i] == self.grid[i+3] == self.grid[i+6]:
                return self.grid[i]

        # Check diagonal 1:
        if self.grid[1] != " " and self.grid[1] == self.grid[5] == self.grid[9]:
            return self.grid[5]
        
        # Check diagonal 2:
        if self.grid[3] != " " and self.grid[3] == self.grid[5] == self.grid[7]:
            return self.grid[5]
        
        return None