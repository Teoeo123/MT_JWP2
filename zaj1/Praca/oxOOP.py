class TicTacToe:
    def __init__(self):
        self.ALL_SPACES = list('123456789')
        self.X, self.O, self.BLANK = 'X', 'O', ' '
        self.board = self.get_blank_board()
        self.current_player, self.next_player = self.X, self.O

    def get_blank_board(self):
        """Tworzy nową, pustą planszę gry."""
        return {space: self.BLANK for space in self.ALL_SPACES}

    def print_board(self):
        """Drukuje planszę gry."""
        board = self.board
        print(f'''
            {board['1']}|{board['2']}|{board['3']} 1 2 3 
            -+-+-
            {board['4']}|{board['5']}|{board['6']} 4 5 6 
            -+-+-
            {board['7']}|{board['8']}|{board['9']} 7 8 9''')

    def is_valid_space(self, space):
        """Sprawdza, czy ruch jest możliwy do wykonania."""
        return space in self.ALL_SPACES and self.board[space] == self.BLANK

    def is_winner(self, player):
        """Sprawdza, czy gracz wygrał."""
        b, p = self.board, player
        return ((b['1'] == b['2'] == b['3'] == p) or
                (b['4'] == b['5'] == b['6'] == p) or
                (b['7'] == b['8'] == b['9'] == p) or
                (b['1'] == b['4'] == b['7'] == p) or
                (b['2'] == b['5'] == b['8'] == p) or
                (b['3'] == b['6'] == b['9'] == p) or
                (b['3'] == b['5'] == b['7'] == p) or
                (b['1'] == b['5'] == b['9'] == p))

    def is_board_full(self):
        """Sprawdza, czy plansza jest pełna."""
        return all(self.board[space] != self.BLANK for space in self.ALL_SPACES)

    def make_move(self, space):
        """Aktualizuje planszę po ruchu gracza."""
        self.board[space] = self.current_player

    def switch_player(self):
        """Zmienia gracza."""
        self.current_player, self.next_player = self.next_player, self.current_player

    def play_game(self):
        """Rozpoczyna grę w kółko i krzyżyk."""
        print('Witaj w grze kółko i krzyżyk!')
        while True:
            self.print_board()
            move = None
            while move not in self.ALL_SPACES or not self.is_valid_space(move):
                move = input(f'Jaki jest ruch gracza {self.current_player}? (1-9) ')
            self.make_move(move)
            if self.is_winner(self.current_player):
                self.print_board()
                print(f'{self.current_player} wygrał grę!')
                break
            elif self.is_board_full():
                self.print_board()
                print('Gra zakończyła się remisem!')
                break
            self.switch_player()
        print('Dziękuję za grę!')

if __name__ == '__main__':
    game = TicTacToe()
    game.play_game()
