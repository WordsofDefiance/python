from random import randrange

# Chutes and Ladders

class Square:
    counter = 0
    def __init__(self):
        self.position = Square.counter
        self.portal = 0
        Square.counter += 1

class Player:
    counter = 0
    def __init__(self, name):
        self.id = 0
        self.name = name
        self.position = 0
        Player.counter += 1

    def spin(self):
        self.position += randrange(1,6)


def createPortals(count, board, rangeMin, rangeMax, portalChangeMin, portalChangeMax):
    counter = count
    while counter >= 0:
        position = randrange(rangeMin, rangeMax)
        portalChange = randrange(portalChangeMin, portalChangeMax)
        # only create portals on Squares that don't have them
        if board[position].portal == 0:
            board[position].portal = portalChange
        counter -= 1

# Create the board
board = []
for number in range(100):
    board.append(Square())


# Create 25 random chutes and ladders
createPortals(5, board, 40, 60, -15, 15)
createPortals(5, board, 10, 90, -8, 8)
createPortals(5, board, 70, 90, -20, 9)
createPortals(5, board, 15, 30, -5, 40)
createPortals(5, board, 25, 50, -15, 35)

# Create some players
player1 = Player("David")
player2 = Player("Kim")
player3 = Player("Trillian")
player4 = Player("Rosie")

players = [player1, player2, player3, player4]


# PLAY THE GAME

gameStatus = True
while gameStatus:
    for player in players:
        if gameStatus == True:
            if player.position < 100:
                player.spin()
                if player.position < 100:
                    player.position += board[player.position].portal
                    print('Player {} is at position {}, portal value: {}'.format(player.name, player.position,board[player.position].portal))
                else:
                    print('Player {} is at position {}, portal value: 0'.format(player.name, player.position))

            else:
                print('Player {} wins!!!!!'.format(player.name))
                gameStatus = False
