import numpy as np
import psonic as ps
import maze as mz
import random


def block_generation(n,s):
    B = np.zeros((n,n))
    B[0][0]=s%n
    for c in range(1,n):
        B[0][c] = (B[0][c-1]+4)%n
    for c in range(n):
        for l in range(1,n):
            B[l][c] = (B[l-1][c]+2)%n
    return B

def board_generation(block,n):
    k,_ = block.shape
    B = []
    for C in range(n*k):
        b = []
        for R in range(n*k):
            b.append(block[C%k][R%k])
        B.append(b)
    return np.array(B)

def play_notes(notes,s=0.15):
    for n in notes:
        d = 0.3+random.random()
        ps.play(70+n,release=d)
        t = ps.random.choice([0.125, 0.25,0, 0.2])
        ps.sleep(t)

if __name__ == '__main__':
    block = block_generation(21,6)
    print(block)
    board = board_generation(block,2)
    print(board.shape)
    n,_ = board.shape
    # L = mz.genera_labirinto(n,n)
    # mz.stampa(L)
    # w = mz.trova_percorso(L,(1,1),(n-1,n-1))
    # print(w)
    # for x in w:
    # 	mz.set_stato(L,x,'Percorso')
    # mz.stampa(L)
    w = [(1, 1), (1, 2), (2, 2), (3, 2), (3, 3), (4, 3), (4, 4), (5, 4), (5, 5), (5, 6), (4, 6), (3, 6), (3, 5), (2, 5), (1, 5), (0, 5), (0, 6), (1, 6), (1, 7), (0, 7), (0, 8), (0, 9), (1, 9), (1, 8), (2, 8), (3, 8), (4, 8), (4, 9), (4, 10), (5, 10), (5, 11), (6, 11), (6, 12), (5, 12), (4, 12), (3, 12), (3, 11), (2, 11), (2, 12), (2, 13), (2, 14), (3, 14), (3, 15), (3, 16), (2, 16), (1, 16), (1, 17), (2, 17), (2, 18), (2, 19), (1, 19), (1, 20), (0, 20), (0, 21), (0, 22), (0, 23), (1, 23), (2, 23), (2, 22), (2, 21), (3, 21), (4, 21), (4, 20), (4, 19), (5, 19), (5, 18), (5, 17), (5, 16), (4, 16), (4, 15), (4, 14), (4, 13), (5, 13), (5, 14), (6, 14), (7, 14), (7, 15), (7, 16), (7, 17), (8, 17), (9, 17), (9, 16), (9, 15), (10, 15), (10, 16), (10, 17), (10, 18), (11, 18), (11, 19), (12, 19), (12, 20), (13, 20), (13, 19), (14, 19), (14, 18), (13, 18), (13, 17), (12, 17), (12, 16), (12, 15), (12, 14), (12, 13), (13, 13), (13, 12), (12, 12), (12, 11), (12, 10), (12, 9), (13, 9), (13, 8), (13, 7), (13, 6), (13, 5), (14, 5), (14, 4), (15, 4), (16, 4), (17, 4), (17, 3), (17, 2), (18, 2), (18, 1), (19, 1), (20, 1), (20, 0), (21, 0), (22, 0), (22, 1), (23, 1), (23, 2), (24, 2), (24, 1), (25, 1), (25, 2), (25, 3), (24, 3), (24, 4), (23, 4), (23, 3), (22, 3), (22, 4), (22, 5), (22, 6), (23, 6), (24, 6), (25, 6), (25, 7), (26, 7), (26, 8), (26, 9), (27, 9), (27, 8), (28, 8), (28, 9), (29, 9), (30, 9), (31, 9), (32, 9), (32, 10), (33, 10), (34, 10), (35, 10), (36, 10), (36, 9), (37, 9), (37, 10), (37, 11), (37, 12), (38, 12), (38, 11), (39, 11), (40, 11), (40, 12), (39, 12), (39, 13), (38, 13), (38, 14), (37, 14), (36, 14), (36, 13), (36, 12), (36, 11), (35, 11), (34, 11), (33, 11), (32, 11), (31, 11), (31, 12), (30, 12), (29, 12), (29, 13), (30, 13), (30, 14), (29, 14), (28, 14), (28, 15), (27, 15), (27, 14), (27, 13), (27, 12), (26, 12), (26, 13), (25, 13), (25, 12), (24, 12), (24, 13), (24, 14), (24, 15), (25, 15), (25, 16), (24, 16), (24, 17), (24, 18), (24, 19), (24, 20), (23, 20), (23, 21), (23, 22), (24, 22), (24, 23), (24, 24), (23, 24), (23, 25), (23, 26), (23, 27), (22, 27), (22, 28), (22, 29), (21, 29), (21, 30), (21, 31), (20, 31), (19, 31), (19, 32), (18, 32), (18, 31), (18, 30), (17, 30), (16, 30), (15, 30), (14, 30), (14, 29), (15, 29), (15, 28), (15, 27), (14, 27), (13, 27), (13, 26), (12, 26), (12, 27), (12, 28), (11, 28), (11, 29), (12, 29), (12, 30), (11, 30), (11, 31), (10, 31), (10, 30), (10, 29), (9, 29), (9, 28), (8, 28), (7, 28), (6, 28), (5, 28), (5, 29), (5, 30), (4, 30), (4, 31), (5, 31), (6, 31), (7, 31), (7, 32), (8, 32), (8, 33), (9, 33), (9, 34), (10, 34), (11, 34), (11, 35), (11, 36), (10, 36), (10, 37), (9, 37), (8, 37), (8, 38), (7, 38), (7, 37), (7, 36), (6, 36), (5, 36), (5, 37), (5, 38), (4, 38), (3, 38), (2, 38), (2, 39), (3, 39), (3, 40), (4, 40), (5, 40), (6, 40), (7, 40), (8, 40), (9, 40), (10, 40), (10, 41), (11, 41), (11, 40), (11, 39), (12, 39), (12, 38), (12, 37), (12, 36), (13, 36), (13, 35), (13, 34), (14, 34), (14, 33), (15, 33), (15, 34), (15, 35), (15, 36), (16, 36), (17, 36), (17, 37), (17, 38), (16, 38), (15, 38), (15, 39), (14, 39), (14, 40), (14, 41), (15, 41), (16, 41), (17, 41), (17, 40), (18, 40), (19, 40), (19, 39), (20, 39), (20, 40), (21, 40), (22, 40), (23, 40), (24, 40), (25, 40), (25, 41), (26, 41), (26, 40), (27, 40), (27, 41), (28, 41), (28, 40), (28, 39), (29, 39), (29, 38), (30, 38), (30, 39), (31, 39), (32, 39), (33, 39), (33, 38), (34, 38), (34, 37), (35, 37), (35, 36), (35, 35), (36, 35), (37, 35), (37, 36), (37, 37), (38, 37), (38, 38), (39, 38), (39, 37), (40, 37), (40, 36), (41, 36), (41, 37), (41, 38), (40, 38), (40, 39), (40, 40), (41, 40), (41, 41)]
    notes = [board[c][r] for (c,r) in w]
    play_notes(notes)