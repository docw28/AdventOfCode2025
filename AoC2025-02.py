import math
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
    length = len(value)
    for div_size in range(1, math.floor(length/2)+1):  # need to check all subdivisions that are at most half the size of the value
        if length % div_size == 0:                     # and only those that will divide evenly
            # print("Division Size: ",div_size)
            i = 0
            while True:
                s1, e1 = i, i+div_size # first comparison subdivision
                s2, e2 = i+div_size, i+div_size+div_size
                # print(value[s1:e1],",",value[s2:e2])
                if value[s1:e1] == value[s2:e2]:
                    i += div_size
                elif i >= (length-div_size):
                    return False
                else:
                    break
    return True

#----------------------------------------------
#data = ingester(test_input)
data = ingester(puzzle_input)

for r in data:
 for value in r:
        # print(value)
        if not valid_ID(value):
            total += value
print("Total of all invalid IDs is: ", total)
