
import time
start_time = time.time()
test_input = """.......S.......\n...............\n.......^.......\n...............\n......^.^......\n...............\n.....^.^.^.....\n...............\n....^.^...^....\n...............\n...^.^...^.^...\n...............\n..^...^.....^..\n...............\n.^.^.^.^.^...^.\n..............."""
puzzle_input = str(open("Day7Input.txt").read())

def ingester(string):
    array = []
    for row in string.split("\n"):
        array.append(list(row))
    return array

def display(array):
    string = ""
    for i in range(len(array)):
        string = string + "\n"
        for j in range(len(array[i])):
            string = string + array[i][j]
    print(string)

def beam_splitter(array):
    splits = 0
    for i in range(len(array)): # i = row
        for j in range(len(array[i])): # j = column
            if array[i][j] == "S" or array[i][j] == "|":
                if (i + 1) < len(array):
                    if array[i+1][j] == ".":
                        array[i+1][j] = "|"
                    elif array[i+1][j] == "^":
                        splits += 1
                        if (j-1) >= 0:
                            array[i+1][j-1] = "|"
                        if (j+1) < len(array[i]):
                            array[i+1][j+1] = "|"
    display(array)
    return splits


#input = ingester(test_input)
input = ingester(puzzle_input)
print(beam_splitter(input))
print("Completion time: ", round((time.time() - start_time)*1000), "ms")