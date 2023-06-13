import random

board = []
board_a = []
gems = 0

def initBoard(x, y):
  global gems
  gem_rate = 5
  for i in range(y):
    row = []
    row2 = []
    for j in range(x):
      roll = random.randint(0,gem_rate)
      if roll == 0:
        row.append("💎")
        gems += 1
      else:
        row.append("🧱")
      row2.append("🌑")
    board.append(row2)
    board_a.append(row)

def displayBoard():
  for row in board:
    line = " "
    for column in row:
      line += column + " "
    print(line)
  print("There are", gems, "gems")

def clearX(x, posX, posY):
  global board, board_a
  left = posX - x
  right = posX + x
  if left < 0:
    left = 0
  if right >= len(board[posY]):
    right = len(board[posY])-1
  for i in range(left, right+1):
    board[posY][i] = board_a[posY][i]


def clearY(y, posX, posY):
  global board, board_a
  top = posY - y
  bot = posY + y
  if top < 0:
    top = 0
  if bot >= len(board):
    bot = len(board)-1
  for i in range(top, bot+1):
    board[i][posX] = board_a[i][posX]