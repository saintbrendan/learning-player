from HState import HState
from HState import WB
from HPlayer1 import HPlayer1
from HPlayer2 import HPlayer2

playerFromColor = {WB.W: HPlayer1, WB.B: HPlayer2}

def runMatch(playerx, playery):
    s = HState()
    while not s.isGameOver():
        p = s.currentPlayerColor
        player = playerFromColor[p]
        print(player)
        moves = s.generateMoves()
        print(len(moves))
        s = player.chooseMove(moves)
        print(s)

    winner = s.getWinner()
    print(f'{winner} is the winner')
