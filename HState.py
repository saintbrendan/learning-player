from enum import Enum
import copy


class WB(Enum):
    empty = 1
    W = 2
    B = 3

    def toString(self):
        if self == WB.W:
            return 'W'
        if self == WB.B:
            return 'B'
        return ' '

    def getWinRank(self):
        if self == WB.W:
            return 0
        return 2

    def direction(self):
        if self == WB.W:
            return -1
        return 1


class HState:
    def __init__(self):
        self.grid = [
            [WB.B, WB.B, WB.B],
            [WB.empty, WB.empty, WB.empty],
            [WB.W, WB.W, WB.W],
        ]
        self.currentPlayerColor = WB.W

    @staticmethod
    def staticmethod():
        return 'static method called'

    def isGameOver(self):
        for color in [WB.W, WB.B]:
            winRank = color.getWinRank()
            if self.grid[winRank][0] == color or self.grid[winRank][1] == color or self.grid[winRank][2] == color:
                print(f'color {color} got to winrank {winRank}')
                return True
        moves = self.generateMoves()
        if len(moves) == 0:
            print ("zero moves")
            return True
        return False

    def getWinner(self):
        for color in [WB.W, WB.B]:
            winRank = color.getWinRank()
            if self.grid[winRank][0] == color or self.grid[winRank][1] == color or self.grid[winRank][2] == color:
                return color
            moves = self.generateMoves()
            if len(moves) == 0:  # current winner lost
                return otherPlayerColor(self.currentPlayerColor)
        raise Exception("Called getWinner() when there wasn't a winner yet")

    def generateMoves(self):
        moves = []
        currentPlayerColor = self.currentPlayerColor
        direction = currentPlayerColor.direction()
        for row in range(3):
            if row == currentPlayerColor.getWinRank():
                continue
            for col in range(3):
                if self.grid[row][col] == currentPlayerColor:
                    # move forward
                    if self.grid[row+direction][col] == WB.empty:
                        newState = copy.deepcopy(self)
                        newState.grid[row][col] = WB.empty
                        newState.grid[row+direction][col] = self.currentPlayerColor
                        newState.currentPlayerColor = otherPlayerColor(self.currentPlayerColor)
                        moves.append(newState)
                    ### TODO: collapse following two steps into range(-1,2,2) loop
                    if col-1 >= 0:
                        if self.grid[row + direction][col-1] == otherPlayerColor(currentPlayerColor):
                            newState = copy.deepcopy(self)
                            newState.grid[row][col] = WB.empty
                            newState.grid[row + direction][col-1] = self.currentPlayerColor
                            newState.currentPlayerColor = otherPlayerColor(self.currentPlayerColor)
                            moves.append(newState)

                    if col+1 < 3:
                        if self.grid[row + direction][col+1] == otherPlayerColor(currentPlayerColor):
                            newState = copy.deepcopy(self)
                            newState.grid[row][col] = WB.empty
                            newState.grid[row + direction][col+1] = self.currentPlayerColor
                            newState.currentPlayerColor = otherPlayerColor(self.currentPlayerColor)
                            moves.append(newState)
        return moves

    def __str__(self):
        s = ""
        for row in self.grid:
            s += '['
            for col in row:
                s += col.toString()
            s += "]\n"
        return s


def otherPlayerColor(player):
    if player == WB.W:
        return WB.B
    return WB.W
