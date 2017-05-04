import os
import time
import itertools

in_file_path = os.path.join(os.path.dirname(__file__), "submitInput.txt")
out_file_path = os.path.join(os.path.dirname(__file__), "testOutput.txt")

with open(in_file_path, 'r') as infile:
    with open(out_file_path, 'w') as outfile:
        cases = int(infile.readline())
        for case in range(cases):
            start = time.time()
            '''
            Triangle Inequality Theorem: the sum of two side lengths of a
            triangle is always greater than the third side.
            '''
            sides = [int(i) for i in infile.readline().split()]  # lista con los lados para el triángulo
            min_perimeter = 0
            del sides[0]  # borro primer elemento porque no interesa y puede dar problemas
            sides.sort()
            for a, b, c in itertools.combinations(sides, 3):
                # print(a, b, c)
                if a + b > c and b + c > a and a + c > b:
                    min_perimeter = a + b + c
                    break
            if min_perimeter == 0:
                runtime = time.time() - start
                # print("Case #" + str(case + 1) + ": " + "IMPOSSIBLE | " + str(runtime))
                outfile.write("Case #" + str(case + 1) + ": " + "IMPOSSIBLE" + "\n")
            else:
                runtime = time.time() - start
                # print("Case #" + str(case + 1) + ": " + str(min_perimeter) + " | " +str(runtime))
                outfile.write("Case #" + str(case + 1) + ": " + str(min_perimeter) + "\n")
