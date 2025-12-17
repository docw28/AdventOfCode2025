import time
start_time = time.time()
test_input = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"""
puzzle_input = str(open("Day10Input.txt").read())

machines = []

class Machine:
    def __init__(self, indicator_light_diagram, button_wiring_schematics, joltage_requirements):
        self.indicator_light_diagram = indicator_light_diagram
        self.button_wiring_schematics = button_wiring_schematics
        self.joltage_requirements = joltage_requirements
        self.indicator_lights = ["."] * len(indicator_light_diagram)

def ingester(string):
    array_of_machines = []

    for line in string.split("\n"):
        machine_parts = line.split(" ")

        light_indicator_diagram = list(machine_parts[0][1:-1]) # "[.##.]" => ['.', '#', '#', '.']
        machine_parts.pop(0)

        joltage_requirements = machine_parts[len(machine_parts)-1][1:-1].split(",") # "{3,5,4,7}" => ['3', '5', '4', '7']
        machine_parts.pop(len(machine_parts)-1)

        button_wiring_schematics = []
        for schematic in machine_parts:
            button_wiring_schematics.append(schematic[1:-1].split(","))

        array_of_machines.append(Machine(light_indicator_diagram, button_wiring_schematics, joltage_requirements))

    return array_of_machines

input = ingester(test_input)


print("Completion time: ", round((time.time() - start_time)*1000), "ms")