'''
This file contains the Game class which represents the Gomoku game logic.
'''
class Game:
    def __init__(self):
        self.board = [[0] * 15 for _ in range(15)]
        self.current_player = 1
    def is_valid_move(self, x, y):
        return self.board[y][x] == 0
    def make_move(self, x, y):
        self.board[y][x] = self.current_player
        self.current_player = 3 - self.current_player
    def is_winner(self, x, y):
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
        for dx, dy in directions:
            count = 1
            count += self.count_in_direction(x, y, dx, dy)
            count += self.count_in_direction(x, y, -dx, -dy)
            if count >= 5:
                return True
        return False
    def count_in_direction(self, x, y, dx, dy):
        count = 0
        player = self.board[y][x]
        while True:
            x += dx
            y += dy
            if x < 0 or x >= 15 or y < 0 or y >= 15 or self.board[y][x] != player:
                break
            count += 1
        return count
    def reset(self):
        self.board = [[0] * 15 for _ in range(15)]
        self.current_player = 1