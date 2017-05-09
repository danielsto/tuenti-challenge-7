import os
import time
import itertools

in_file_path = os.path.join(os.path.dirname(__file__), "submitInput.txt")
out_file_path = os.path.join(os.path.dirname(__file__), "testOutput.txt")

start = time.time()
with open(in_file_path, 'r') as infile:
    with open(out_file_path, 'w') as outfile:

        cases = int(infile.readline())

        for case in range(cases):
            sides = [int(i) for i in infile.readline().split()]
            min_perimeter = 0
            del sides[0]
            sides.sort()
            for a, b, c in itertools.combinations(sides, 3):
                if a + b > c and b + c > a and a + c > b:
                    min_perimeter = a + b + c
                    break

            if min_perimeter == 0:
                outfile.write(
                    "Case #" + str(case + 1) + ": " + "IMPOSSIBLE" + "\n")
            else:
                outfile.write("Case #" + str(case + 1) + ": " + str(
                    min_perimeter) + "\n")

        runtime = time.time() - start
        print(runtime)
