c = [[0 for i in range(8)] for i in range(8)]
pawn, night, bishop, rook, queen, king = (1, 2, 3, 4, 5, 6)

# Sets up the pieces
def pieceSetup():
    # White pieces
    c[0][0] = rook
    c[0][1] = night
    c[0][2] = bishop
    c[0][3] = queen
    c[0][4] = king
    c[0][5] = bishop
    c[0][6] = night
    c[0][7] = rook

    # Pawns
    i = 0
    while i < 8:
        c[1][i] = pawn
        i += 1

    # Black pieces
    c[7][0] = rook
    c[7][1] = night
    c[7][2] = bishop
    c[7][3] = queen
    c[7][4] = king
    c[7][5] = bishop
    c[7][6] = night
    c[7][7] = rook

    # Pawns
    i = 0
    while i < 8:
        c[6][i] = pawn
        i += 1

def movePiece():
    moveFromString = input("Piece to move: ")
    moveToString = input("Where to move it: ")
    rows = "abcdefgh"

    # Find the piece to move
    moveFromLetter = moveFromString[0]
    yMoveFrom = int(rows.find(moveFromLetter))
    xMoveFrom = int(moveFromString[1]) - 1

    # Find where to move the piece
    moveToLetter = moveToString[0]
    yMoveTo = int(rows.find(moveToLetter))
    xMoveTo = int(moveToString[1]) - 1

    c[xMoveTo][yMoveTo] = c[xMoveFrom][yMoveFrom]
    c[xMoveFrom][yMoveFrom] = 0

pieceSetup()

# Play the game
while True:
    i = 7
    while i > -1:
        print(c[i])
        i -= 1
    movePiece()
