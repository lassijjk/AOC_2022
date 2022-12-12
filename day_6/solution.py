
d = open("data.txt")

def search_for_unique(data , length):
    for i in range(len(data)-length):
        signal = data[i:i+length]
        if len(set(signal)) == len(signal):
            return i+length

data = d.read()
print(search_for_unique(data, 4))
print(search_for_unique(data, 14))


