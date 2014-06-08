import os
import sys
from PIL import *
from PIL import Image
from PIL import ImageFilter

# Directories and other state variables
pieces_dir = "piece_images/"

# Coordinates of board in chess.com
# 42, 230 (left, top corner)
# 309, 496 (left, bottom corner)
# Width:267
# Height:266
# Width / Height of each position:33.375

# 209 261

piece_dim = 45
left_x, left_y = 128, 252
right_x, right_y = left_x + piece_dim * 8, left_y + piece_dim * 8
w, h = right_x-left_x, left_y-right_y

def set_board_coordinates(should_prompt=True):
    global piece_dim, left_x, left_y, right_x, right_y, w, h
    if should_prompt:
        print("Enter the upper left corner of the chess board: (x, y)")
        x, y = tuple(int(x) for x in sys.stdin.readline().split())
    else:
        x, y = left_x, left_y
    piece_dim = int(33.25)
    left_x, left_y = x, y
    right_x, right_y = left_x + piece_dim * 8, left_y + piece_dim * 8
    w, h = right_x-left_x, left_y-right_y

def capture_screen(out_name):
    os.system("screencapture " + out_name)

def capture_board(screen_name, out_name):
    img = Image.open(screen_name)
    box = (left_x, left_y, right_x, right_y)
    board = img.crop(box)
    board.save(out_name, 'png')

def segment_board(chess_board_name, outline=False):
    img = Image.open(chess_board_name)
    for i in range(8):
        for j in range(8):
            x, y = i * piece_dim, j * piece_dim
            box = (x, y, x + piece_dim, y + piece_dim)
            piece = img.crop(box)
            if outline:
                piece = piece.filter(ImageFilter.FIND_EDGES)
                piece = piece.convert('1')
            piece.save(pieces_dir + str(i) + str(j), "png")

if __name__=="__main__":
    set_board_coordinates()
    capture_screen("capture_screen_test")
    capture_board("capture_screen_test", "chess_board_test")
    segment_board("chess_board_test")
