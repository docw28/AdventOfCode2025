# L = -, R = +. get new number then +100 if <0 or -100 if >99?
test_input = """L68\nL30\nR48\nL5\nR60\nL55\nL1\nL99\nR14\nL82"""
puzzle_input = str(open("Day1Input.txt").read())
default_pos = 50
current_pos = default_pos
prev_pos = current_pos
password = 0

def ingester(string):
    
    instructions = []
    instructions = string.split("\n")
    for i in range(len(instructions)):
        instructions[i] = [instructions[i][0],int(instructions[i][1:])]
    #we now have an array of instructions in the format ["L", 99]
    return instructions
    
def dialer(current_pos, instruction):
    z_clicks = 0
    for i in range(instruction[1]):
        if instruction[0] == "L":
            current_pos -= 1
            if current_pos < 0:
                current_pos += 100
        elif instruction[0] =="R":
            current_pos += 1
            if current_pos > 99:
                current_pos -= 100
        if current_pos == 0:
            z_clicks += 1
    return current_pos, z_clicks

#-------------------------------------------------
#instructions = ingester(test_input)
instructions = ingester(puzzle_input)

for i in range(len(instructions)):
    dial_result = dialer(current_pos, instructions[i])
    current_pos = dial_result[0]
    print(instructions[i], prev_pos, current_pos, dial_result[1])
    password += dial_result[1]
    prev_pos = current_pos
        
print("\nPassword: ", password)