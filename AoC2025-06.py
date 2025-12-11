import time
start_time = time.time()
test_input = "123 328  51 64 \n 45 64  387 23 \n  6 98  215 314\n*   +   *   +  "
puzzle_input = str(open("Day6Input.txt").read())
total = 0

def ingester(string):
    input_array = []
    equations_array = []
    equations = 0
    rows = string.split("\n")
    for row in rows:
        input_array.append(row.split())
    print(input_array)
    equations = len(input_array[0])
    print(equations)
    for i in range(equations):
        equations_array.append([]) 
    print(equations_array)
    for i in range(equations):
        for j in range(len(input_array)):
            equations_array[i].append(input_array[j][i])
    return equations_array
    
def equation_solver(equation):
    result = 0
    if equation[len(equation)-1] == "+":
        equation.pop()
        for number in equation:
            result += int(number)
    elif equation[len(equation)-1] == "*":
        equation.pop()
        result = 1
        for number in equation:
            result *= int(number)
    return result

#input = ingester(test_input)
input = ingester(puzzle_input)
print(input)


for equation in input:
    total += equation_solver(equation)


print("Total: ", total)
print("Completion time: ", round((time.time() - start_time)*1000), "ms")