from functools import lru_cache

with open('03.in', 'r') as f:
    lines = f.read().strip().split('\n')

def process_line(line):
    max_num = 0
    for i in range(len(line)):
        for j in range(i + 1, len(line)):
            num = int(line[i] + line[j])
            if num > max_num:
                max_num = num

    return max_num

@lru_cache
def process_line_p2(line, idx, used):
    if idx == len(line) and used == 12:
        return 0
    if idx == len(line):
        return -10**20
    answer = process_line_p2(line, idx+1, used)
    if used < 12:
        answer = max(answer, 10**(11-used) * int(line[idx]) + process_line_p2(line, idx + 1, used + 1))
    return answer

sum_p1, sum_p2 = 0, 0
for line in lines:
    sum_p1 += process_line(line)
    sum_p2 += process_line_p2(line, 0, 0)

print(sum_p1, sum_p2)