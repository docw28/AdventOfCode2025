import time
start_time = time.time()
test_input = "987654321111111\n811111111111119\n234234234234278\n818181911112111"
puzzle_input = str(open("Day3Input.txt").read())
jolt_total_2 = 0
jolt_total_12 = 0

def ingester(string):                       # ingest lines of numbers into 2D array of banks of batteries
    array = []
    for line in string.split("\n"):
        array.append(list(line))
    return array


def find_highest_joltage(bank,batt_no):     # given a bank and a max number of batteries, find the highest possible joltage
    highest_joltage = ""
    while len(bank) > batt_no:
        

    


    return int(highest_joltage)

#banks = ingester(test_input)
banks = ingester(puzzle_input)


for bank in banks:
    #jolt_total_2 += find_highest_joltage(bank,2)
    jolt_total_12 += find_highest_joltage(bank,12)

print("Total of highest joltage using 2 batteries in each bank is: ",jolt_total_2)
print("Total of highest joltage using 12 batteries in each bank is: ",jolt_total_12)
print("Completion time: ", round((time.time() - start_time)*1000), "ms")