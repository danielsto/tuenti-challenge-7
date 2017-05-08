import os
import math

in_file_path = os.path.join(os.path.dirname(__file__), "submitInput.txt")
out_file_path = os.path.join(os.path.dirname(__file__), "testOutput.txt")

with open(in_file_path, 'r') as infile:
    with open(out_file_path, 'w') as outfile:
        cases = int(infile.readline())

        for case in range(cases):
            next(infile)
            hunger = list(map(int, (infile.readline().split())))
            slices = sum(hunger)
            pizzas = math.ceil(slices / 8)

            outfile.write("Case #" + str(case + 1) + ": " + str(pizzas) + "\n")
