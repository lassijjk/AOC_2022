

def range_contains_range(r1, r2):
    return r1.start>=r2.start and r1.stop<=r2.stop or r1.start<=r2.start and r1.stop>=r2.stop


with open('day_4/data') as d:
    lines = [line.rstrip('\n') for line in d.readlines()]
    

contain_result, overlap_result = 0, 0

for line in lines:
    elves = [range(int(pair[0]), int(pair[1])+1) for pair in [pair.split('-') for pair in line.split(',')]]
    contain_result += 1 if range_contains_range(elves[0], elves[1]) else 0
    overlap_result += 1 if set(elves[0]).intersection(set(elves[1])) else 0
    
print(contain_result, overlap_result)
