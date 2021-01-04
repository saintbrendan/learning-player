from TState import TState
from TState import XO
from TPlayer1 import TPlayer1
from TPlayer2 import TPlayer2

playerLookup = {XO.X: TPlayer1, XO.O: TPlayer2}

def runMatch(playerx, playery):
    s = TState()
    while not s.isGameOver():
        p = s.currentPlayer
        player = playerLookup[p]
        print(player)
        moves = s.generateMoves()
        print(len(moves))
        s = player.chooseMove(moves)
        print(s)

    winner = s.getWinner()
    print(f'{winner} is the winner')
