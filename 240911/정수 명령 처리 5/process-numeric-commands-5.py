class DynamicArray:
    def __init__(self):
        self.array = []

    def push_back(self, value):
        self.array.append(value)

    def pop_back(self):
        if self.array:
            self.array.pop()

    def size(self):
        return len(self.array)

    def get(self, k):
        if 1 <= k <= len(self.array):
            return self.array[k - 1]  # 1-based index
        return None

def process_commands(commands):
    dynamic_array = DynamicArray()
    results = []

    for command in commands:
        parts = command.split()

        if parts[0] == "push_back":
            dynamic_array.push_back(int(parts[1]))
        elif parts[0] == "pop_back":
            dynamic_array.pop_back()
        elif parts[0] == "size":
            results.append(dynamic_array.size())
        elif parts[0] == "get":
            k = int(parts[1])
            results.append(dynamic_array.get(k))

    return results

# 입력 처리
n = int(input())
commands = [input().strip() for _ in range(n)]

# 명령어 처리
results = process_commands(commands)

# 출력
for result in results:
    print(result)