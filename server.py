# Doesn't actually work because need LONG algebraic notation

import sys
from bottle import route, run, template, get, post, request, static_file
import urllib
import json
import click
import chess_screen_capture
import chess_interface
import chess_ai
import time
from random import randint
import commands

def startup():
    player = sys.stdin.readline().strip()
    if player == "BLACK":
        print("PLAYING AS BLACK")
        chess_ai.TURN = chess_ai.BLACK
    else:
        print("PLAYING AS WHITE")
        chess_ai.TURN = chess_ai.WHITE

@route("/", method="GET")
def receive_chess_moves():
    moves = json.loads(request.query['moves'])
    moves = [x for x in moves if x != u'']
    move_list = ""
    count, index = 0, 0

    #print(moves)
    if chess_ai.TURN == chess_ai.WHITE:
        if len(moves) % 2 == 1:
            return
    if chess_ai.TURN == chess_ai.BLACK:
        if len(moves) % 2 == 0:
            return
    
    for move in moves:
        if index % 2 == 0:
            count += 1
            move_list += str(count) + "."
        move_list += move + " "
        index += 1
    #print("SAN movelist")
    #print(move_list)
    move_list += " *"
    
    pgn_file = open("moves.pgn", 'w')
    pgn_file.write(move_list)
    pgn_file.close()

    lan = commands.getstatusoutput("./pgn-extract -C --notags -Wuci moves.pgn")
    lan = lan[1].split()[2:-7]
    #print("LAN: " + str(lan))

    lan_move_list = ""
    for move in lan:
        lan_move_list += move + " "

    #print("Filtered List: " + lan_move_list)
    mv = chess_ai.get_move2(lan_move_list)
    pt = chess_ai.get_move_pts(mv)
    time.sleep(randint(1, 10) / float(randint(5, 10)))
    chess_ai.make_move(pt)

startup()
run(host='localhost', port=8080, quiet=True)
