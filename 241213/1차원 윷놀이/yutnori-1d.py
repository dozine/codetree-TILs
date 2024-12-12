def backtrack(turn, positions, score, moves, m, k, max_score):
    """
    백트래킹 함수
    turn: 현재 턴 (0부터 시작)
    positions: 각 말의 현재 위치를 저장한 리스트
    score: 현재까지 획득한 점수
    moves: 각 턴에서 주어진 이동 거리 리스트
    m: 윷놀이 판의 길이
    k: 말의 수
    max_score: 최대 점수
    """
    # 모든 턴이 끝난 경우 최대 점수 갱신
    if turn == len(moves):
        max_score[0] = max(max_score[0], score)
        return
    
    # 현재 턴의 이동 거리
    move = moves[turn]

    # 모든 말을 대상으로 이동 시도
    for i in range(k):
        # 현재 말의 위치 저장
        current_pos = positions[i]
        
        # 말이 이미 m번 지점에 도달한 경우
        if current_pos == m:
            continue
        
        # 말을 이동
        new_pos = current_pos + move
        if new_pos >= m:  # m번 지점을 초과한 경우
            new_pos = m
        
        # 상태 업데이트 및 백트래킹 호출
        positions[i] = new_pos
        additional_score = 1 if new_pos == m else 0
        backtrack(turn + 1, positions, score + additional_score, moves, m, k, max_score)
        
        # 상태 복원
        positions[i] = current_pos


def maximize_score(n, m, k, moves):
    """
    주어진 조건에서 얻을 수 있는 최대 점수를 계산합니다.
    n: 턴의 수
    m: 윷놀이 판의 길이
    k: 말의 수
    moves: 각 턴에서 주어진 이동 거리 리스트
    """
    # 초기 상태
    positions = [1] * k  # 모든 말은 1번 지점에서 시작
    max_score = [0]      # 최대 점수 저장 (mutable로 전달)
    
    # 백트래킹 시작
    backtrack(0, positions, 0, moves, m, k, max_score)
    
    return max_score[0]


# 입력 처리
def main():
    # 첫 번째 줄 입력
    n, m, k = map(int, input().split())
    # 두 번째 줄 입력
    moves = list(map(int, input().split()))
    
    # 최대 점수 계산
    result = maximize_score(n, m, k, moves)
    print(result)


if __name__ == "__main__":
    main()
