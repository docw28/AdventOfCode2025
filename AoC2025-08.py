import time
import math as m
start_time = time.time()
test_input = """162,817,812\n57,618,57\n906,360,560\n592,479,940\n352,342,300\n466,668,158\n542,29,236\n431,825,988\n739,650,466\n52,470,668\n216,146,977\n819,987,18\n117,168,530\n805,96,715\n346,949,466\n970,615,88\n941,993,340\n862,61,35\n984,92,344\n425,690,689"""
puzzle_input = str(open("Day8Input.txt").read())

def ingester(string):
    array = []
    for row in string.split("\n"):
        array.append(row.split(","))
    return array

input = ingester(test_input)
print(input)

def straight_line_distance(array1,array2):
    distance = 0
    for i in range(3):
        array1[i] = int(array1[i])
        array2[i] = int(array2[i])
    [x1,y1,z1] = array1
    [x2,y2,z2] = array2
    x_dist = abs(x1-x2)
    y_dist = abs(y1-y2)
    z_dist = abs(z1-z2)
    distance = m.sqrt(x_dist**2 + y_dist**2 + z_dist**2)
    return distance



print(straight_line_distance(input[0],input[1]))



print("Completion time: ", round((time.time() - start_time)*1000), "ms")