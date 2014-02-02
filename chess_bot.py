import sys
import click
import chess_screen_capture
import chess_interface
import chess_ai
import time
from random import randint

# x, y = 620, 40
# click.mouse_click(x, y)
# click.mouse_click(x, y)

if __name__=="__main__":
    print("Enter in which color you are playing as: ")
    player = sys.stdin.readline().strip()
    if player == "BLACK":
        print("PLAYING AS BLACK")
        chess_ai.TURN = chess_ai.BLACK
    else:
        print("PLAYING AS WHITE")
        chess_ai.TURN = chess_ai.WHITE

    chess_screen_capture.set_board_coordinates(False)
    
    last_position = ""
    double_check = 1
    while True:
        b = chess_interface.get_board_abrs()
        fen = chess_ai.getFEN(b)
        if fen != last_position:
            if double_check == 0:
                print("Double checked... Making move")
                mv = chess_ai.get_move(fen)
                pt = chess_ai.get_move_pts(mv)
                chess_ai.make_move(pt)
                time.sleep(.2)
                b = chess_interface.get_board_abrs()
                last_position = chess_ai.getFEN(b)
                double_check = 1
            else:
                print("Double checking board configuration...")
                double_check -= 1
        else:
            print("No move was made: Passing")
