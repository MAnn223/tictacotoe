from random import randrange

q = True

#creates board
def DisplayBoard(board):
    dashes = '+'
    row2 = '|'
    numRow = ['|', '|', '|', '|']
    for x in range(3):
        for i in range(7):
            dashes += '-'
            row2 += ' '
        dashes += '+'
        row2 += '|'

    for rows in range(3):
        for x in range(3):
            for i in range(8):
                if i == 7:
                    numRow[rows] += '|'
                elif i != 3:
                    numRow[rows] += ' '
                else:
                    numRow[rows] += str(board[rows][x])

    for i in range(3):
        print(dashes)
        print(row2)
        print(numRow[i])
        print(row2)
    print(dashes)




#takes user's input and makes a move
def EnterMove(board):
    x = True
    while x == True:
        uMove = input("Enter a number 1-9 where you would like to draw an 'O': ")
        uMoveNum = int(uMove)
        boardNums = ''
        row = 0
        column = 0
        r = uMoveNum % 3
        qt = uMoveNum // 3
        for i in board:
            for j in board:
                boardNums += str(j)
        if uMove in boardNums:
            if r == 0:
                row = qt - 1
                column = 2
            else:
                row = qt
                column = r - 1
            board[row][column] = 'O'
            x = False
        else:
            print('That square is taken, enter again')



#checks for victory and who has won
def VictoryFor(board, sign):
    if (board[0][0] == sign and board[0][1] == sign and board[0][2] == sign) or (board[0][0] == sign and board[1][
        0] == sign and board[2][0] == sign) or (board[1][0] == sign and board[1][1]==sign and board[1][2]==sign) or (board[0][
        0] == sign and board[1][1] == sign and board[2][2] == sign) or (board[2][0] == sign and board[2][1] == sign and
        board[2][2] == sign) or (board[0][0] == sign and board[1][0] == sign and board[2][0] == sign) or (board[0][2] == sign and board[1][2] == sign and board[2][2] == sign) :
        print(sign, ' has won')
        return True


#computer's move
def DrawMove(board):
    z = True
    while z == True:
        randNum = randrange(1, 10)
        boardNumsComp = ''
        rowC = 0
        columnC = 0
        rC = randNum % 3
        qtC = randNum // 3
        for i in board:
            for j in board:
                boardNumsComp += str(j)
        if str(randNum) in boardNumsComp:
            if rC == 0:
                rowC = qtC - 1
                columnC = 2
            else:
                rowC = qtC
                columnC = rC - 1
            board[rowC][columnC] = 'X'
            z = False
        else:
            continue

#game code using the functions
board = [[1, 2, 3], [4, 'X', 6], [7, 8, 9]]
compSign = 'X'
uSign = 'O'
while q == True:
    DisplayBoard(board)
    EnterMove(board)
    if VictoryFor(board, 'X') == True:
        DisplayBoard(board)
        break
    if VictoryFor(board, 'O') == True:
        DisplayBoard(board)
        break
    DrawMove(board)
    if VictoryFor(board, 'X') == True:
        DisplayBoard(board)
        break
    if VictoryFor(board, 'O') == True:
        DisplayBoard(board)

        break
