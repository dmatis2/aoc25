with open('02.in', 'r') as f:
    ranges = f.read().split(',')

valid_ranges = []

for r in ranges:
    start, end = r.split('-')
    if len(start) == len(end) and len(start) % 2 != 0:
        continue
    valid_ranges.append((start, end))

def part1():
    count = 0
    for (r1, r2) in valid_ranges:
        r1, r2 = int(r1), int(r2)
        for i in range(r1, r2 + 1):
            if len(str(i)) % 2 != 0:
                continue
            i_str = str(i)
            l = len(i_str) // 2
            if i_str[:l] == i_str[l:]:
                count += i
    return count

def part2():
    count = 0
    all_ranges = list(map(lambda x: x.split('-'), ranges))
    for (r1, r2) in all_ranges:
        r1, r2 = int(r1), int(r2)
        for i in range(r1, r2 + 1):
            i_str = str(i)
            for k in range(2, len(i_str)+1):
                if len(i_str)%k == 0:
                    possible = True
                    mid = len(i_str)//k
                    l = 0
                    while l < len(i_str):
                        if i_str[l:l+mid] != i_str[:mid]:
                            possible = False
                        l += mid
                    if possible:
                        count += i
                        break
    return count

print(part1())
print(part2())