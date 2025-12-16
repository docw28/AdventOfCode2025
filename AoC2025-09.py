import time
import math as m
start_time = time.time()
test_input = "7,1\n11,1\n11,7\n9,7\n9,5\n2,5\n2,3\n7,3"
puzzle_input = str(open("Day9Input.txt").read())

def ingester(string):
    array = []
    array = string.split("\n")

    for i in range(len(array)):
        array[i] = array[i].split(",")
        array[i][0] = int(array[i][0])
        array[i][1] = int(array[i][1])
        
    return array

def hypotenuse(coord1, coord2):
    x1, y1 = coord1[0], coord1[1]
    x2, y2 = coord2[0], coord2[1]
    number = m.sqrt(abs(x1-x2)**2 + abs(y1-y2)**2)

    return number

def area(coord1, coord2):
    x1, y1 = coord1[0], coord1[1]
    x2, y2 = coord2[0], coord2[1]
    number = (abs(x1-x2)+1) * (abs(y1-y2)+1)
    return number

input = ingester(test_input)

largest_distance = 0
largest_area = 0
for coord1 in input:
    for coord2 in input:
        hyp = hypotenuse(coord1, coord2)
        if hyp > largest_distance:
            largest_distance = hyp
            largest_area = area(coord1,coord2)

print("Largest possible rectangle: ", largest_area, "units^2")
print("Completion time: ", round((time.time() - start_time)*1000), "ms")