import time
start_time = time.time()
test_input = "987654321111111\n811111111111119\n234234234234278\n818181911112111"
puzzle_input = str(open("Day3Input.txt").read())
jolt_total = 0

def ingester(string):
    array = []
    for line in string.split("\n"):
        array.append(list(line))
    return array

def find_highest_joltage(bank):
    highest_joltage = 0
    for i in range(len(bank)-1):
        for j in range(i+1,len(bank)):
            joltage = int(bank[i]+bank[j])
            if joltage > highest_joltage:
                highest_joltage = joltage



    return highest_joltage

banks = ingester(test_input)

for bank in banks:
    jolt_total += find_highest_joltage(bank)

print("Total of highest joltage in each bank is: ",jolt_total)
print("Completion time: ", round((time.time() - start_time)*1000), "ms")