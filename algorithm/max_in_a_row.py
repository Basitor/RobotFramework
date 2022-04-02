from copy import deepcopy

data = [
    ["orange", "blue", "yellow", "orange", "orange"],
    ["orange", "blue", "blue", "yellow", "blue"],
    ["blue", "yellow", "blue", "blue", "yellow", "yellow", "blue"],
    ["blue", "blue"],
    ["blue", "blue", "blue", "yellow", "blue"],
    ["blue", "blue", "blue", "yellow", "blue"],
    ["blue", "yellow", "blue", "blue", "yellow", "yellow", "blue"],

]

max_len = max([len(row) for row in data])
same_len_data = [[None for _ in range(max_len)]]

for row in data:
    same_len_data.append([None] + row + [None for _ in range(max_len - len(row))])

length = [[1 for _ in range(max_len)] for _ in range(len(same_len_data))]
length2 = deepcopy(length)

for row in range(1, len(same_len_data)):
    for col in range(1, max_len):
        if same_len_data[row][col] and same_len_data[row][col - 1] == same_len_data[row][col]:
            length[row][col] = length[row][col - 1] + 1
        if same_len_data[row][col] and same_len_data[row - 1][col] == same_len_data[row][col]:
            length2[row][col] = length2[row - 1][col] + 1

max_a = max([max(i) for i in length])
max_b = max([max(i) for i in length2])

print(max(max_a, max_b))
