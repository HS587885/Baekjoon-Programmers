from collections import deque

def bfs(start_r, start_c, board, visited, target):
    moves = [(1,0), (-1,0), (0,1), (0,-1)]
    q = deque()
    q.append((start_r, start_c))
    visited[start_r][start_c] = True
    cells = [(start_r, start_c)]

    while q:
        r, c = q.popleft()
        for dr, dc in moves:
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(board) and 0 <= nc < len(board) and not visited[nr][nc]:
                if board[nr][nc] == target:
                    visited[nr][nc] = True
                    q.append((nr, nc))
                    cells.append((nr, nc))

    # 좌표를 가장 왼쪽 위 기준 상대좌표로 변환
    min_r = min(x for x,y in cells)
    min_c = min(y for x,y in cells)
    normalized = sorted([(x - min_r, y - min_c) for x, y in cells])
    return normalized

def rotate(piece):
    # 90도 회전: (x, y) -> (y, -x)
    rotated = [(y, -x) for x, y in piece]
    # 다시 가장 왼쪽 위 기준으로 맞춤
    min_x = min(x for x, y in rotated)
    min_y = min(y for x, y in rotated)
    normalized = sorted([(x - min_x, y - min_y) for x, y in rotated])
    return normalized

def solution(game_board, table):
    n = len(game_board)
    visited_board = [[False]*n for _ in range(n)]
    visited_table = [[False]*n for _ in range(n)]

    blanks = []  # 게임 보드 빈칸 모양 리스트
    blocks = []  # 테이블 조각 모양 리스트

    # 1. 게임 보드에서 빈칸(0) 모양 추출
    for i in range(n):
        for j in range(n):
            if game_board[i][j] == 0 and not visited_board[i][j]:
                blanks.append(bfs(i, j, game_board, visited_board, 0))

    # 2. 테이블에서 조각(1) 모양 추출
    for i in range(n):
        for j in range(n):
            if table[i][j] == 1 and not visited_table[i][j]:
                blocks.append(bfs(i, j, table, visited_table, 1))

    answer = 0
    used = [False]*len(blocks)  # 블록 사용 여부 표시

    # 3. 빈칸과 조각을 비교하며 맞추기
    for blank in blanks:
        matched = False
        for i, block in enumerate(blocks):
            if used[i]:
                continue
            for _ in range(4):  # 4번 회전 시도
                if blank == block:
                    answer += len(block)
                    used[i] = True
                    matched = True
                    break
                block = rotate(block)
            if matched:
                break

    return answer


