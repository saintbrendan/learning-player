from enum import Enum
import copy


class XO(Enum):
    empty = 1
    X = 2
    O = 3

    def toString(self):
        if self == XO.X:
            return 'X'
        if self == XO.O:
            return 'O'
        return ' '



class TState:
    def __init__(self):
        self.grid = [
            [XO.empty, XO.empty, XO.empty],
            [XO.empty, XO.empty, XO.empty],
            [XO.empty, XO.empty, XO.empty],
        ]
        self.currentPlayer = XO.X

    @staticmethod
    def staticmethod():
        return 'static method called'

    def isGameOver(self):
        for player in [XO.X, XO.O]:
            if self.grid[0][0] == player and self.grid[1][1] == player and self.grid[2][2] == player :
                return True
            if self.grid[0][2] == player and self.grid[1][1] == player and self.grid[2][0] == player:
                return True
            for i in range(3):
                if self.grid[i][0] == player and self.grid[i][1] == player and self.grid[i][2] == player:
                    return True
                if self.grid[0][i] == player and self.grid[1][i] == player and self.grid[2][i] == player:
                    return True
        return False

    def getWinner(self):
        for player in [XO.X, XO.O]:
            if self.grid[0][0] == player and self.grid[1][1] == player and self.grid[2][2] == player :
                return player
            if self.grid[0][2] == player and self.grid[1][1] == player and self.grid[2][0] == player:
                return player
            for i in range(3):
                if self.grid[i][0] == player and self.grid[i][1] == player and self.grid[i][2] == player:
                    return player
                if self.grid[0][i] == player and self.grid[1][i] == player and self.grid[2][i] == player:
                    return player
        raise Exception("Called getWinner() when there wasn't a winner yet")

    def generateMoves(self):
        moves = []
        for row in range(3):
            for col in range(3):
                if self.grid[row][col] == XO.empty:
                    newState = copy.deepcopy(self)
                    newState.grid[row][col] = self.currentPlayer
                    newState.currentPlayer = otherPlayer(self.currentPlayer)
                    moves.append(newState)
        return moves

    def __str__(self):
        s = ""
        for row in self.grid:
            s+='['
            for col in row:
                s += col.toString()
            s += "]\n"
        return s



def otherPlayer(player):
    if player == XO.X:
        return XO.O
    return XO.X

