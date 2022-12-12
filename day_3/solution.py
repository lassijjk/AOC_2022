import string

with open('day_3/data') as d:
    lines = [line.rstrip('\n') for line in d.readlines()]

letters = [*string.ascii_letters]

result_p1 = result_p2 = 0

for line in lines:
    first, second = [*line[:len(line)//2]], [*line[len(line)//2:]]
    result_p1 += [letters.index(item) for item in first if second.count(item) > 0][0]+1

for i in range(0, len(lines), 3):
    first, second, third = lines[i:i+3]
    result_p2 += [letters.index(item) for item in first if (second.count(item) > 0 and third.count(item) > 0)][0] + 1
print(result_p1, result_p2)