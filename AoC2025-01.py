# L = -, R = +. get new number then +100 if <0 or -100 if >99?
test_input = """L68\nL30\nR48\nL5\nR60\nL55\nL1\nL99\nR14\nL82"""
puzzle_input = str(open("Day1Input.txt").read())
default_pos = 50
current_pos = default_pos
password = 0

def ingester(string):
    
    instructions = []
    instructions = string.split("\n")
    for i in range(len(instructions)-1):
        print(i, instructions[i])
        instructions[i] = [instructions[i][0],int(instructions[i][1:])]
    #we now have an array of instructions in the format ["L", 99]
    return instructions
    
def dialer(current_pos, instruction):
    
    if instruction[0] == "L":           # simulate a turn to the left or right
        current_pos -= instruction[1]
    elif instruction[0] == "R":
        current_pos += instruction[1]
    else:
        print("bruh?")
        
    while current_pos < 0:                 # correct for looping set of numbers
        current_pos += 100
    while current_pos > 99:
        current_pos -= 100
    return current_pos

#-------------------------------------------------
#instructions = ingester(test_input)
instructions = ingester(puzzle_input)

for i in range(len(instructions)-1):
    current_pos = dialer(current_pos, instructions[i])
    print(current_pos)
    if current_pos == 0:
        password += 1
        
print("\nPassword: ", password)