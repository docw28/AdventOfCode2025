test_input = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
# total of invalids for test_input: 1227775554
puzzle_input = str(open("Day2Input.txt").read())
total = 0


def ingester(input):
    ID_ranges = input.split(",")
    for i in range(len(ID_ranges)):
        ID_ranges[i] = ID_ranges[i].split("-")
        ID_ranges[i] = list(range(int(ID_ranges[i][0]),int(ID_ranges[i][1])+1))
    return ID_ranges

def valid_ID(value):
    value = str(value)
    halves = []
    val_length = len(value)
    if ((val_length) % 2) != 0:
        return True
    halves.append(value[int(val_length/2):])
    halves.append(value[:int(val_length/2)])
    return halves









#----------------------------------------------
data = ingester(test_input)
#data = ingester(puzzle_input)

print(valid_ID(11))
"""for range in data:
    for value in range:
        if not valid_ID(value):
            total += value"""
print("Total of all invalid IDs is: ", total)
