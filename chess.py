from tkinter import *
from PIL import ImageTk,Image

width = 720
widthPerPiece = width / 8

root = Tk()
canvas = Canvas(root, width = width, height = width)
canvas.pack()


knightImage = ImageTk.PhotoImage(Image.open("horse.jpg"))
blackSquareImage = ImageTk.PhotoImage(Image.open("blackSquare.png"))
whiteSquareImage = ImageTk.PhotoImage(Image.open("whiteSquare.png"))

c = [[0 for i in range(8)] for i in range(8)]
pawn, night, bishop, rook, queen, king = (1, 2, 3, 4, 5, 6)

def spawnImage(xCoord, yCoord, img):
    canvas.create_image(translateXCoord(xCoord), translateYCoord(yCoord), anchor=NW, image=img)

def spawnSquare(xCoord, yCoord):
    if yCoord % 2 == 0:
        if xCoord % 2 == 0:
            canvas.create_image(translateXCoord(xCoord), translateYCoord(yCoord), anchor=NW, image=blackSquareImage)
        elif xCoord % 2 != 0:
            canvas.create_image(translateXCoord(xCoord), translateYCoord(yCoord), anchor=NW, image=whiteSquareImage)
    elif yCoord % 2 != 0:
        if xCoord % 2 != 0:
            canvas.create_image(translateXCoord(xCoord), translateYCoord(yCoord), anchor=NW, image=blackSquareImage)
        elif xCoord % 2 == 0:
            canvas.create_image(translateXCoord(xCoord), translateYCoord(yCoord), anchor=NW, image=whiteSquareImage)
            
def translateXCoord(xCoord):
    xCoordInPixels = xCoord * widthPerPiece
    translatedXCoord = xCoordInPixels
    return translatedXCoord

def translateYCoord(yCoord):
    yCoordInPixels = (yCoord + 1) * widthPerPiece
    translatedYCoord = width - yCoordInPixels
    return translatedYCoord

def squareSetup():
    i = 0
    while i < len(c):
        i += 1
        j = 0
        while j < len(c):
            spawnSquare(i-1, j)
            j += 1

def pieceImageSetup():
    spawnImage()

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
    xMoveFrom = int(rows.find(moveFromLetter))
    yMoveFrom = int(moveFromString[1]) - 1

    # Find where to move the piece
    moveToLetter = moveToString[0]
    xMoveTo = int(rows.find(moveToLetter))
    yMoveTo = int(moveToString[1]) - 1

    c[yMoveTo][xMoveTo] = c[yMoveFrom][xMoveFrom]
    c[yMoveFrom][xMoveFrom] = 0

    # Draw the picture
    canvas.create_image(translateXCoord(xMoveTo), translateYCoord(yMoveTo), anchor=NW, image=knightImage)
    spawnSquare(xMoveFrom, yMoveFrom)

squareSetup()
pieceSetup()

# Play the game
while True:
    i = 7
    while i > -1:
        print(c[i])
        i -= 1
    movePiece()