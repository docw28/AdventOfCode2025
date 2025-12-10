import time
start_time = time.time()
test_input = "3-5\n10-14\n16-20\n12-18\n\n1\n5\n8\n11\n17\n32"
puzzle_input = str(open("Day5Input.txt").read())
total_fresh = 0

def ingester(string):
    string = string.split("\n\n")
    fresh_ranges = string[0].split("\n")
    for i in range(len(fresh_ranges)):
        fresh_ranges[i] = fresh_ranges[i].split("-")
    food_IDs = string[1].split("\n")
    return fresh_ranges,food_IDs

def ID_fresh(food_ID,fresh_ranges):
    for ID_range in fresh_ranges:
        #print(ID_range)
        if int(ID_range[0]) <= int(food_ID) <= int(ID_range[1]):
            return True
    return False  

#input = ingester(test_input)
input = ingester(puzzle_input)

for food_ID in input[1]:
    #print(food_ID)
    if ID_fresh(food_ID, input[0]):
        total_fresh += 1
        #print("Ding!")



print("Total number of fresh IDs is: ", total_fresh)
print("Completion time: ", round((time.time() - start_time)*1000), "ms")