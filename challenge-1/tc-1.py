import os
import math

in_file_path = os.path.join(os.path.dirname(__file__), "submitInput.txt")
out_file_path = os.path.join(os.path.dirname(__file__), "testOutput.txt")

with open(in_file_path, 'r') as infile:
    with open(out_file_path, 'w') as outfile:
        cases = infile.readline()
        for case in range(int(cases)):
            case_n = " ".join(infile.readline().split())
            hunger_1 = (infile.readline().split())
            slices = 0
            for sliced in hunger_1:
                slices = slices + int(sliced)
            pizzas = slices / 8
            outfile.write("Case #" + str(case + 1) + ": " + str(math.ceil(pizzas)) + "\n")
