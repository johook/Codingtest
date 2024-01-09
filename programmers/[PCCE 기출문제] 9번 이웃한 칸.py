def isokay(h_check,w_check,n):
    if 0<=h_check<n and 0<=w_check<n:
        return 1
    return 0

def solution(board, h, w):
    n = len(board)
    count = 0
    dh = [-1,1,0,0]
    dw = [0,0,-1,1]
    for i in range(4):
        h_check = h+dh[i]
        w_check = w+dw[i]
        if isokay(h_check,w_check,n):
            if board[h][w] == board[h_check][w_check]:
                count+=1  
    answer = count
    return answer

