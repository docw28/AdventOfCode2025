import time
start_time = time.time()
# L = -, R = +. get new number then +100 if <0 or -100 if >99?
test_input = """L68\nL30\nR48\nL5\nR60\nL55\nL1\nL99\nR14\nL82"""
puzzle_input = str(open("Day1Input.txt").read())
default_pos = 50
current_pos = default_pos
password_1,password_2 = 0,0

def ingester(string):
    
    instructions = []
    instructions = string.split("\n")
    for i in range(len(instructions)):
        # print(instructions[i])
        instructions[i] = [instructions[i][0],int(instructions[i][1:])]
    #we now have an array of instructions in the format ["L", 99]
    return instructions
    
def dialer(current_pos, instruction):
    zero_clicks = 0
    #print(instruction)
    if instruction[0] == "L":           # simulate a turn to the left or right
        if current_pos == 0:
            zero_clicks -= 1
            #print("anticlick", end="")
        current_pos -= instruction[1]
    elif instruction[0] == "R":
        current_pos += instruction[1]
    else:
        print("bruh?")
    
    while current_pos < 0:                 # correct for looping set of numbers
        current_pos += 100
        zero_clicks += 1
        #print("click!")
    while current_pos > 99:
        current_pos -= 100
        zero_clicks += 1
        #print("click!")
    return current_pos, zero_clicks

#-------------------------------------------------
#instructions = ingester(test_input)
instructions = ingester(puzzle_input)

for i in range(len(instructions)):
    #print("\n")
    current_pos,zero_clicks = dialer(current_pos, instructions[i])
    # zero_clicks = dialer(current_pos, instructions[i])[1]
    #print(current_pos)
    if current_pos == 0:
        #print("click!")
        password_1 += 1
        if instructions[i][0] == "L":
            password_2 += 1
    password_2 += zero_clicks
        
print("\nPassword 1: ", password_1)
print("Password 2: ", password_2)
print("Completion time: ", round((time.time() - start_time) * 1000), "ms")