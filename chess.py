from tkinter import *
from PIL import ImageTk,Image

width = 720
widthPerPiece = width / 8

root = Tk()
canvas = Canvas(root, width = width, height = width)
canvas.pack()


whiteRookImage = ImageTk.PhotoImage(Image.open("whiteRook.jpg"))
blackRookImage = ImageTk.PhotoImage(Image.open("blackRook.jpg"))
whiteKnightImage = ImageTk.PhotoImage(Image.open("whiteHorse.jpg"))
blackKnightImage = ImageTk.PhotoImage(Image.open("blackHorse.jpg"))
whiteBishopImage = ImageTk.PhotoImage(Image.open("whiteBishop.jpg"))
blackBishopImage = ImageTk.PhotoImage(Image.open("blackBishop.jpg"))
whiteQueenImage = ImageTk.PhotoImage(Image.open("whiteQueen.jpg"))
blackQueenImage = ImageTk.PhotoImage(Image.open("blackQueen.jpg"))
whiteKingImage = ImageTk.PhotoImage(Image.open("whiteKing.jpg"))
blackKingImage = ImageTk.PhotoImage(Image.open("blackKing.jpg"))
whitePawnImage = ImageTk.PhotoImage(Image.open("whitePawn.jpg"))
blackPawnImage = ImageTk.PhotoImage(Image.open("blackPawn.jpg"))

pieceImages = [whitePawnImage, whiteKnightImage, whiteBishopImage, whiteRookImage, whiteQueenImage, whiteKingImage, blackPawnImage, blackKnightImage, blackBishopImage, blackRookImage, blackQueenImage, blackKingImage]

blackSquareImage = ImageTk.PhotoImage(Image.open("blackSquare.png"))
whiteSquareImage = ImageTk.PhotoImage(Image.open("whiteSquare.png"))

c = [[0 for i in range(8)] for i in range(8)]
whitePawn, whiteNight, whiteBishop, whiteRook, whiteQueen, whiteKing, blackPawn, blackNight, blackBishop, blackRook, blackQueen, blackKing = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)

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
    # White pieces
    spawnImage(0, 0, whiteRookImage)
    spawnImage(1, 0, whiteKnightImage)
    spawnImage(2, 0, whiteBishopImage)
    spawnImage(3, 0, whiteQueenImage)
    spawnImage(4, 0, whiteKingImage)
    spawnImage(5, 0, whiteBishopImage)
    spawnImage(6, 0, whiteKnightImage)
    spawnImage(7, 0, whiteRookImage)

    for i in range(8):
        spawnImage(i, 1, whitePawnImage)
        i += 1
    
    # Black pieces
    spawnImage(0, 7, blackRookImage)
    spawnImage(1, 7, blackKnightImage)
    spawnImage(2, 7, blackBishopImage)
    spawnImage(3, 7, blackQueenImage)
    spawnImage(4, 7, blackKingImage)
    spawnImage(5, 7, blackBishopImage)
    spawnImage(6, 7, blackKnightImage)
    spawnImage(7, 7, blackRookImage)

    for i in range(8):
        spawnImage(i, 6, blackPawnImage)
        i += 1

# Sets up the pieces
def pieceSetup():
    # White pieces
    c[0][0] = whiteRook
    c[0][1] = whiteNight
    c[0][2] = whiteBishop
    c[0][3] = whiteQueen
    c[0][4] = whiteKing
    c[0][5] = whiteBishop
    c[0][6] = whiteNight
    c[0][7] = whiteRook

    # Pawns
    for i in range(8):
        c[1][i] = whitePawn
        i += 1

    # Black pieces
    c[7][0] = blackRook
    c[7][1] = blackNight
    c[7][2] = blackBishop
    c[7][3] = blackQueen
    c[7][4] = blackKing
    c[7][5] = blackBishop
    c[7][6] = blackNight
    c[7][7] = blackRook

    # Pawns
    for i in range(8):
        c[6][i] = blackPawn
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

    # Move the piece
    c[yMoveTo][xMoveTo] = c[yMoveFrom][xMoveFrom]

    # Draw the picture
    spawnImage(xMoveTo, yMoveTo, pieceImages[int(c[yMoveFrom][xMoveFrom]) - 1])
    spawnSquare(xMoveFrom, yMoveFrom)
    
    c[yMoveFrom][xMoveFrom] = 0

squareSetup()
pieceImageSetup()
pieceSetup()

# Play the game
while True:
    i = 7
    while i > -1:
        print(c[i])
        i -= 1
    try:
        movePiece()
    except:
        while True:
            print("\n\n\n\n\n")
            continueMessage = input('You cannot and shall not do that, you fool! \nWould you please write "I am dumb and foolish, and shall never do that unresponsible and stupid action again" to continue? ')
            if continueMessage == "I am dumb and foolish, and shall never do that unresponsible and stupid action again":
                break