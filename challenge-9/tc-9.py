import os
import math

in_file_path = os.path.join(os.path.dirname(__file__), "submitInput.txt")
out_file_path = os.path.join(os.path.dirname(__file__), "testOutput.txt")

with open(in_file_path, 'r') as infile:
    with open(out_file_path, 'w') as outfile:
        cases = int(infile.readline())

        for case in range(cases):
            sections = infile.readline().split()
            s = int(sections[0])  # Straight sections
            c = int(sections[1])  # 90 deg curves
            d = int(sections[2])  # Double straights

            used_c = math.trunc(c / 2) * 2

            if used_c < 4:  # minimum of 4 curves to close circuit
                used_c = 0
                used_s = 0
                used_d = 0
            elif used_c == 4:
                used_s = math.trunc(s / 2) * 2
                if s >= 2:
                    used_d = d
                else:
                    used_d = math.trunc(d / 2) * 2
            elif (used_c - 2) % 4 == 0 and s >= 2:
                used_s = math.trunc(s / 2) * 2
                used_d = d
            elif used_c == 8 and (s >= 2 or d >= 1):
                used_s = math.trunc(s / 2) * 2
                used_d = d
            elif used_c >= 12 and used_c % 4 == 0:
                used_s = math.trunc(s / 2) * 2
                used_d = d
            used_c -= 2

            outfile.write("Case #" + str(case + 1) + ": " + str(
                used_c + used_s + used_d) + "\n")
