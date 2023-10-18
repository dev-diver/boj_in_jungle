import copy
N=int(input())
def set(n,row,board):
    ans = 0
    for col in range(n):
        cond=True
        for ro,co in enumerate(board):
            if(col==co or co-ro==col-row or ro+co==row+col):
                cond = False
                break
        if not cond: continue
        board[row]=col
        if row==n-1 : return 1
        ans += set(n,row+1,copy.copy(board))
    return ans

board = [-100]*N
result = set(N,0,board)
print(result)