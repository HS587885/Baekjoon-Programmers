def solution(board):
    rows = len(board)
    cols = len(board[0])
    total = rows * cols
    
    if all(0 not in row for row in board):
        return 0
    
    new_board = [row[:] for row in board]
    
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == 1:
                for box in range(max(0, i-1), min(rows, i+2)):
                    for num in range(max(0, j-1), min(cols, j+2)):
                        new_board[box][num] = 1
    
    return sum(row.count(0) for row in new_board)

                
                
                
                    
                    
                
    
    
                
      