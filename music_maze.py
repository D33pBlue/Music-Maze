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
    board = board_generation(block,4)
    print(board.shape)
    n,_ = board.shape
    L = mz.make_maze(n,n)
    e1 = L[0][0]
    e2 = L[n-1][n-1]
    w = mz.find_path(e1,e2)
    for x in w:
    	x['state'] = 'Path'
    # mz.show(L)
    notes = [board[x['c']][x['r']] for x in w]
    play_notes(notes)
