
import time
start_time = time.time()
test_input = "..@@.@@@@.\n@@@.@.@.@@\n@@@@@.@.@@\n@.@@@@..@.\n@@.@@@@.@@\n.@@@@@@@.@\n.@.@.@.@@@\n@.@@@.@@@@\n.@@@@@@@@.\n@.@.@@@.@."
puzzle_input = str(open("Day4Input.txt").read())
retrievable_rolls = 0

def ingester(string):
    string = string.split("\n")
    for i in range(len(string)):
        string[i] = list(string[i])
    return string

def rolls_around(array, row, col):
    count = 0
    for i in range(-1,2):
        for j in range(-1,2):
            in_row_bounds = row + i >= 0 and row + i < len(array)
            in_col_counds = col + j >= 0 and col + j < len(array[row])
            not_middle = not (i == 0 and j == 0)
            if in_row_bounds and in_col_counds and not_middle:
                if array[row + i][col + j] == "@":
                    count += 1
    return count

#input = ingester(test_input)
input = ingester(puzzle_input)

for row in range(len(input)):
    for column in range(len(input[row])):
        if input[row][column] == "@" and rolls_around(input, row, column) < 4:
            retrievable_rolls += 1

print("Retrievable rolls: ", retrievable_rolls)
print("Completion time: ", round((time.time() - start_time)*1000), "ms")