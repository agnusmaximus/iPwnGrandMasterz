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
from Chessnut import Game

chessgame = Game(fen="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")

def startup():
    player = sys.stdin.readline().strip()
    if player == "BLACK":
        print("PLAYING AS BLACK")
        chess_ai.TURN = chess_ai.BLACK
    else:
        print("PLAYING AS WHITE")
        chess_ai.TURN = chess_ai.WHITE

    if chess_ai.TURN == chess_ai.WHITE:
        mv = chess_ai.get_move2("")
        pt = chess_ai.get_move_pts(mv)
        chess_ai.make_move(pt)

@route("/", method="GET")
def receive_chess_moves():
    moves = json.loads(request.query['moves'])
    move_list = ""
    for move in moves:
        move_list += move + " "
    print(move_list)

    mv = chess_ai.get_move2(move_list)
    pt = chess_ai.get_move_pts(mv)
    chess_ai.make_move(pt)

startup()
run(host='localhost', port=8080)
