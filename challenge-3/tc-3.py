import os
import math
in_file_path = os.path.join(os.path.dirname(__file__), "testInput.txt")
out_file_path = os.path.join(os.path.dirname(__file__), "testOutput.txt")

with open(in_file_path, 'r') as infile:
    with open(out_file_path, 'w') as outfile:

        cases = infile.readline()

        for case in range(int(cases)):
            points = int(infile.readline())
            cards = math.ceil(math.log(points, 2))

            outfile.write("Case #" + str(case + 1) + ": " + str(cards) + "\n")
