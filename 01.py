with open('01.in', 'r') as f:
    lines = f.read().split('\n')

def part1():
    pos = 50
    count = 0
    for line in lines:
        dir, dist = line[0], int(line[1:])
        pos += -dist if dir == 'L' else dist
        pos %= 100

        if pos == 0:
            count += 1
    return count

def part2():
    count = 0
    pos = 50
    for line in lines:
        dir, dist = line[0], int(line[1:])
        if dist >= 100:
            count += dist // 100
            dist = dist % 100
        old = pos
        pos += -dist if dir == 'L' else dist
        
        if (pos <= 0 or pos >= 100) and old != 0:
            count += 1
        pos %= 100
    return count

print(f'Part 1: {part1()}')
print(f'Part 2: {part2()}')