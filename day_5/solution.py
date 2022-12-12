import re


def read_file(): 
    with open('data.txt') as d:
        data = d.read()
    setting = data.split("\n\n")[0].split("\n")
    moves = data.split("\n\n")[1].split("\n")
    return setting, moves


def parse_setting(setting):
    crate_structure = [[] for i in range(9)]
    for line in reversed(setting[:-1]):
        for i in range(0, 35, 4):
            crate = line[i:i+4]
            parsed_crate = re.sub(r"[][ ]", "", crate)
            if parsed_crate != "":
                crate_structure[i//4].append(parsed_crate)
    return crate_structure


def parse_moves(moves):
    parsed_moves = []
    for line in moves:
        if line != "":
            parsed_moves.append([int(n) for n in line.strip("move ").replace("from ", "").replace("to ", "").split(" ")])
    return parsed_moves


def do_instructions(crates, instructions):
    for instruction in instructions:
        crates_to_be_moved = crates[instruction[1]-1][-instruction[0]:]
        crates[instruction[1]-1] = crates[instruction[1]-1][:-instruction[0]]
        crates_to_be_moved.reverse() # Comment this out for p2
        crates[instruction[2]-1].extend(crates_to_be_moved)
    return crates


setting, moves = read_file()
crates = parse_setting(setting)
instructions = parse_moves(moves)
moved_crates = do_instructions(crates, instructions)
for crate in moved_crates:
    print(crate[-1])