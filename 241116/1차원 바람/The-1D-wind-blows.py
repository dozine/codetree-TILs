def shift_row(arr, direction):
    if direction == 'L':
        return [arr[-1]] + arr[:-1]
    else:
        return arr[1:] + [arr[0]]

def propagate_wind(building, row, direction):
    curr_row = row
    shift_direction = 'R' if direction == 'L' else 'L'
    
    while True:
        building[curr_row] = shift_row(building[curr_row], shift_direction)
        
        if direction == 'L':
            curr_row -= 1
        else:
            curr_row += 1
        
        if curr_row < 0 or curr_row >= len(building):
            break
        
        if any(building[row][i] == building[curr_row][i] for i in range(len(building[0]))):
            continue
        else:
            break

def simulate_wind(building, winds):
    for row, direction in winds:
        propagate_wind(building, int(row) - 1, direction)
    return building

# Read input
N, M, Q = map(int, input().split())
building = [list(map(int, input().split())) for _ in range(N)]
winds = [tuple(input().split()) for _ in range(Q)]

# Simulate wind and print final building
final_building = simulate_wind(building, winds)
for row in final_building:
    print(' '.join(map(str, row)))