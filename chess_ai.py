import sys
import os
import chess_screen_capture
import chess_interface
import commands
import re
import click
from random import randint
from time import sleep

WHITE, BLACK = 0, 1
TURN = WHITE
W_Q_CASTLE, W_K_CASTLE, B_Q_CASTLE, B_K_CASTLE = 1, 1, 1, 1
#W_Q_CASTLE, W_K_CASTLE, B_Q_CASTLE, B_K_CASTLE = 0, 0, 0, 0

def getFEN(b):
        rows = []   
        for i in range(8):
            #row = b[i*8:(i+1)*8]
            row = b[i]
            cnt = 0; res = ""
            for c in row:
                if c == ".":
                    cnt+=1
                else:
                    if cnt: 
                        res += str(cnt); 
                        cnt=0
                    res+=c
            if cnt:
                res += str(cnt)
            rows.append(res)
        board = "/".join(rows)

        turn = (["w","b"])[TURN]

        kq = ""
        if int(W_K_CASTLE): kq+="K"
        if int(W_Q_CASTLE): kq+="Q"
        if int(B_K_CASTLE): kq+="k"
        if int(B_Q_CASTLE): kq+="q"
        if not (W_K_CASTLE or W_Q_CASTLE or B_K_CASTLE or B_Q_CASTLE):
            kq = "-"

        #x = int(v[5])
        #y = int(v[6])
        x, y = 0, 1
        ep = "-"
        """
        if not (x == 0 and y == 0):
            if turn == "b" and (self._board[y][x-1] == 'p' or self._board[y][x+1] == 'p'):
                ep = "%s%s" % ( ("abcdefgh")[x], ("87654321")[y+1])
            elif turn == "w" and (self._board[y][x-1] == 'P' or self._board[y][x+1] == 'P'):
                ep = "%s%s" % ( ("abcdefgh")[x], ("87654321")[y-1])                                   
        
        move = (self._state_stack_pointer+1)/2
        """

        #result = '/'.join(rows) + " " + turn + " " + kq + " " + ep + " " + "0 1"
        result = '/'.join(rows) + " " + turn + " " + kq
        return result

def get_move(fen=""):
    if fen == "":
        b = chess_interface.get_board_abrs()
        fen = getFEN(b)
    print(fen)
    random_depth = str(randint(15, 25))
    print("Random depth: " + random_depth)
    result = commands.getstatusoutput('sh use_stockfish.sh ' + fen + " " + random_depth)[1]
    bests = [x[:4] for x in re.findall("bestmove (.*)", result)]
    print(bests)
    return bests[0]

def get_move2(move_list=""):
    result = commands.getstatusoutput('sh use_stockfish2.sh ' + move_list)
    #print(result)
    bests = [x[:4] for x in re.findall("bestmove (.*)", result[1])]
    #print(bests)
    return bests[0]

def get_move_pts(mv):
    start, end = mv[:2], mv[2:]
    w1, h1 = ord(start[0])-ord('a'), 8-int(start[1])
    w2, h2 = ord(end[0])-ord('a'), 8-int(end[1])

    pt1 = (w1 * 33.375 + chess_screen_capture.left_x + 33.375/2,
           h1 * 33.375 + chess_screen_capture.left_y + 33.375/2)
    pt2 = (w2 * 33.375 + chess_screen_capture.left_x + 33.375/2, 
           h2 * 33.375 + chess_screen_capture.left_y + 33.375/2)

    global W_Q_CASTLE, W_K_CASTLE, B_K_CASTLE, B_Q_CASTLE
    if w1 == 4 and h1 == 7:
        W_Q_CASTLE = 0
        W_K_CASTLE = 0
    if w1 == 0 and h1 == 0:
        B_Q_CASTLE = 0
    if w1 == 7 and h1 == 0:
        B_K_CASTLE = 0
    if w1 == 4 and h1 == 0:
        B_Q_CASTLE = 0
        B_K_CASTLE = 0
    if w1 == 0 and h1 == 7:
        W_Q_CASTLE = 0
    if w1 == 7 and h1 == 7:
        W_K_CASTLE = 0
        
    return (pt1, pt2)

def make_move_test(pt):
    # First click to get into the chess window
    click.mouse_click(pt[0][0], pt[0][1])
    sleep(.5)
    click.mouse_click(pt[0][0], pt[0][1])
    click.mouse_click(pt[1][0], pt[1][1])

def make_move(pt):
    click.mouse_click(pt[0][0], pt[0][1])
    sleep(.5)
    click.mouse_click(pt[0][0], pt[0][1])
    click.mouse_click(pt[1][0], pt[1][1])
    click.mouse_click(1000, 500)
    
if __name__=="__main__":
    mv = get_move()
    pt = get_move_pts(mv)
    make_move_test(pt)
