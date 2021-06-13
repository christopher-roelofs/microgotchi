import board
import analogio



class SytemBoard:
    def __init__(self,board):
        self.board = board
        self.a_button = 2
        self.b_button = 1
        self.start_button = 4
        self.select_button = 8

        if self.board == "pygamer":
            self.a_button = 2
            self.b_button = 1
            self.start_button = 4
            self.select_button = 8

