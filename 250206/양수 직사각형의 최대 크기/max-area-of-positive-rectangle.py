def largest_rectangle_area(heights):
    """히스토그램에서 가장 큰 직사각형의 넓이를 구하는 함수"""
    stack = []
    max_area = 0
    heights.append(0)  # 끝을 표시하기 위한 더미 값 추가

    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
    
    heights.pop()  # 더미 값 제거
    return max_area


def max_positive_rectangle(grid):
    n, m = len(grid), len(grid[0])
    max_area = 0
    heights = [0] * m  # 히스토그램 높이 배열 초기화

    for i in range(n):
        for j in range(m):
            # 연속된 양수 높이 계산
            if grid[i][j] > 0:
                heights[j] += 1
            else:
                heights[j] = 0
        # 현재 행의 히스토그램에서 최대 직사각형 넓이 계산
        max_area = max(max_area, largest_rectangle_area(heights))
    
    return max_area


# 입력
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 최대 양수 직사각형 크기 출력
print(max_positive_rectangle(grid))
