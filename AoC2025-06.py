import time
start_time = time.time()
test_input = "123 328  51 64 \n 45 64  387 23 \n  6 98  215 314\n*   +   *   +  "
puzzle_input = str(open("Day6Input.txt").read())

def ingester(string):
    array = []
    equations = 0
    rows = string.split("\n")
    for row in rows:
        array.append(row.split())
    print(array)
    equations = len(array[0])


input = ingester(test_input)


print("Completion time: ", round((time.time() - start_time)*1000), "ms")