
with open('data') as f:
    rounds = list(filter(None, f.read().split('\n')))
    
combos_p1 = ['BX', 'CY', 'AZ', 'AX', 'BY', 'CZ', 'CX', 'AY', 'BZ']
combos_p2 = ['BX', 'CX', 'AX', 'AY', 'BY', 'CY', 'CZ', 'AZ', 'BZ']
score_p1, score_p2 = 0, 0

for round in rounds:
    line = round.replace(" ", "")
    score_p1 += combos_p1.index(line) + 1 
    score_p2 += combos_p2.index(line) + 1 
    
print(score_p1, score_p2)
