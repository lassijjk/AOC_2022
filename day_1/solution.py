
with open('data') as d:
    lines = d.readlines()

tmp = 0
vectorVictor = []
for line in lines:
    line = line.rstrip('\n')
    if not line:
        vectorVictor.append(tmp)
        tmp = 0
    else:
        tmp += int(line)

print(max(vectorVictor))
print(sorted(vectorVictor, reverse=True)[:3])
print(sum(sorted(vectorVictor, reverse=True)[:3]))