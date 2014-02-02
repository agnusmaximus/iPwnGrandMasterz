import os
import sys
import chess_screen_capture
import chess_img_cmp

# Coordinates of board in chess.com
# 42, 230 (left, top corner)
# 309, 496 (left, bottom corner)
# Width:267
# Height:266
# Width / Height of each position:33.375

piece_dir = "piece_images/"
valid_piece_dir = "piece_images/valid_pieces/"

wht_rks = ['wht_rk1', 'wht_rk2']
wht_knts = ['wht_knt1', 'wht_knt2']
wht_bishs = ['wht_bish1', 'wht_bish2']
wht_pawns = ['wht_pawn1', 'wht_pawn2']
wht_queen = ['wht_queen', 'wht_queen2']
wht_king = ['wht_king', 'wht_king2']

blk_rks = ['blk_rk1', 'blk_rk2']
blk_knts = ['blk_knt1', 'blk_knt2']
blk_bishs = ['blk_bish1', 'blk_bish2']
blk_pawns = ['blk_pawn1', 'blk_pawn2']
blk_queen = ['blk_queen', 'blk_queen2']
blk_king = ['blk_king', 'blk_king2']
empty_pieces = ['empty1', 'empty2']
"""
piece_ids
0 - blk rook
1 - blk knt
2 - blk bish
3 - blk queen
4 - blk king
5 - wht rook
6 - wht knt
7 - wht bish
8 - wht queen
9 - wht king
10 - wht pawn
11 - blk pawn
"""

blk_rk_id = 0
blk_knt_id = 1
blk_bish_id = 2
blk_queen_id = 3
blk_king_id = 4
wht_rk_id = 5
wht_knt_id = 6
wht_bish_id = 7
wht_queen_id = 8
wht_king_id = 9
wht_pawn_id = 10
blk_pawn_id = 11
empty = 12

names_to_ids = {
    "blk_rook" : 0,
    "blk_knt" : 1,
    "blk_bish" : 2,
    "blk_queen" : 3,
    "blk_king" : 4,
    "wht_rook" : 5,
    "wht_knt" : 6,
    "wht_bish" : 7,
    "wht_queen" : 8,
    "wht_king" : 9,
    "wht_pawn" : 10,
    "blk_pawn" : 11,
    "empty" : 12
}

abr_to_ids = {
    "r" : 0,
    "n" : 1,
    "b" : 2,
    "q" : 3,
    "k" : 4,
    "R" : 5,
    "N" : 6,
    "B" : 7,
    "Q" : 8,
    "K" : 9,
    "P" : 10,
    "p" : 11,
    "." : 12
}

ids_to_names  = {v:k for k, v in names_to_ids.items()}
ids_to_abr = {v:k for k, v in abr_to_ids.items()}

def get_piece_refs():
    refs = []
    for i in range(8):
        for j in range(8):
            refs.append(str(j)+str(i))
    return refs

def match_piece(ref):
    m, b_id = -100000000, -1

    a = chess_img_cmp.cmp(piece_dir, valid_piece_dir, ref, wht_rks[0])
    if a > m:
        m = a
        b_id = wht_rk_id
    a = chess_img_cmp.cmp(piece_dir, valid_piece_dir, ref, wht_rks[1])
    if a > m:
        m = a
        b_id = wht_rk_id
    a = chess_img_cmp.cmp(piece_dir, valid_piece_dir, ref, wht_knts[0])
    if a > m:
        m = a
        b_id = wht_knt_id
    a = chess_img_cmp.cmp(piece_dir, valid_piece_dir, ref, wht_knts[1])
    if a > m:
        m = a
        b_id = wht_knt_id
    a = chess_img_cmp.cmp(piece_dir, valid_piece_dir, ref, wht_bishs[0])
    if a > m:
        m = a
        b_id = wht_bish_id
    a = chess_img_cmp.cmp(piece_dir, valid_piece_dir, ref, wht_bishs[1])
    if a > m:
        m = a
        b_id = wht_bish_id
    a = chess_img_cmp.cmp(piece_dir, valid_piece_dir, ref, wht_pawns[0])
    if a > m:
        m = a
        b_id = wht_pawn_id
    a = chess_img_cmp.cmp(piece_dir, valid_piece_dir, ref, wht_pawns[1])
    if a > m:
        m = a
        b_id = wht_pawn_id
    a = chess_img_cmp.cmp(piece_dir, valid_piece_dir, ref, wht_queen[0])
    if a > m:
        m = a
        b_id = wht_queen_id
    a = chess_img_cmp.cmp(piece_dir, valid_piece_dir, ref, wht_queen[1])
    if a > m:
        m = a
        b_id = wht_queen_id
    a = chess_img_cmp.cmp(piece_dir, valid_piece_dir, ref, wht_king[0])
    if a > m:
        m = a
        b_id = wht_king_id
    a = chess_img_cmp.cmp(piece_dir, valid_piece_dir, ref, wht_king[1])
    if a > m:
        m = a
        b_id = wht_king_id
    a = chess_img_cmp.cmp(piece_dir, valid_piece_dir, ref, blk_rks[0])
    if a > m:
        m = a
        b_id = blk_rk_id
    a = chess_img_cmp.cmp(piece_dir, valid_piece_dir, ref, blk_rks[1])
    if a > m:
        m = a
        b_id = blk_rk_id
    a = chess_img_cmp.cmp(piece_dir, valid_piece_dir, ref, blk_knts[0])
    if a > m:
        m = a
        b_id = blk_knt_id
    a = chess_img_cmp.cmp(piece_dir, valid_piece_dir, ref, blk_knts[1])
    if a > m:
        m = a
        b_id = blk_knt_id
    a = chess_img_cmp.cmp(piece_dir, valid_piece_dir, ref, blk_bishs[0])
    if a > m:
        m = a
        b_id = blk_bish_id
    a = chess_img_cmp.cmp(piece_dir, valid_piece_dir, ref, blk_bishs[1])
    if a > m:
        m = a
        b_id = blk_bish_id
    a = chess_img_cmp.cmp(piece_dir, valid_piece_dir, ref, blk_pawns[1])
    if a > m:
        m = a
        b_id = blk_pawn_id
    a = chess_img_cmp.cmp(piece_dir, valid_piece_dir, ref, blk_pawns[0])
    if a > m:
        m = a
        b_id = blk_pawn_id
    a = chess_img_cmp.cmp(piece_dir, valid_piece_dir, ref, blk_queen[0])
    if a > m:
        m = a
        b_id = blk_queen_id
    a = chess_img_cmp.cmp(piece_dir, valid_piece_dir, ref, blk_queen[1])
    if a > m:
        m = a
        b_id = blk_queen_id
    a = chess_img_cmp.cmp(piece_dir, valid_piece_dir, ref, blk_king[0])
    if a > m:
        m = a
        b_id = blk_king_id
    a = chess_img_cmp.cmp(piece_dir, valid_piece_dir, ref, blk_king[1])
    if a > m:
        m = a
        b_id = blk_king_id
    a = chess_img_cmp.cmp(piece_dir, valid_piece_dir, ref, empty_pieces[0])
    if a > m:
        m = a
        b_id = empty
    a = chess_img_cmp.cmp(piece_dir, valid_piece_dir, ref, empty_pieces[1])
    if a > m:
        m = a
        b_id = empty
    return b_id

def get_board():
    chess_screen_capture.capture_screen("screen")
    chess_screen_capture.capture_board("screen", "board")
    chess_screen_capture.segment_board("board")
    refs = []
    board = [[0 for x in range(8)] for x in  range(8)]
    for i in range(8):
        for j in range(8):
            board[j][i] = match_piece(str(i)+str(j))
    return board

def get_board_abrs():
    b = get_board()
    r = [[0 for x in range(8)] for x in range(8)]
    for i in range(8):
        for j in range(8):
            r[i][j] = ids_to_abr[b[i][j]]
    return r
            
def pretty_print(b):
    template = ""
    for i in range(8):
        if i != 0:
            template += "|"
        template += "{"+str(i)+":"+str(5)+"}"
    print(template.format('0', '1', '2', '3', '4', '5', '6', '7'))
    print("==============================================")

    rec = []
    for i in range(8):
        rec.append((ids_to_abr[x] for x in b[i]))
    for recs in rec:
        print template.format(*recs)
    
if __name__=="__main__":
    pretty_print(get_board())
