import os
import time
import itertools

in_file_path = os.path.join(os.path.dirname(__file__), "test.txt")
out_file_path = os.path.join(os.path.dirname(__file__), "testOutput.txt")

with open(in_file_path, 'r') as infile:
    with open(out_file_path, 'w') as outfile:
        cases = int(infile.readline())
        steps = []
        for case in range(cases):
            years = 0
            print("CASE: ", case)
            fs = [int(i) for i in infile.readline().split()]
            print("PARAMETROS: ", fs)
            dest = fs[0]
            shortcuts = fs[1]
            if shortcuts == 0:
                for year in range(dest):
                    years += year
                print("TOTAL: ", years, "\n")
            else:
                for shortcut in range(shortcuts):
                    years = 0
                    shortcut_list = [int(i) for i in infile.readline().split()]
                    print("ATAJO: ", shortcut_list)
                    step_1 = shortcut_list[0]
                    step_2 = shortcut_list[1]
                    cost = shortcut_list[2]
                    for i, year in enumerate(range(dest)):
                        steps.append(i)# print(year+1)
                        if year + 1 < step_1:
                            years += year + 1
                        elif year + 1 == step_1:
                            years += cost
                        elif step_1 < year + 1 < step_2:
                            pass
                        elif year + 1 == dest:
                            break
                        else:
                            years += year + 1
                    if sum(steps) < years:
                        print("TOTAL: ", steps)
                    else:
                        print("TOTAL: ", years)
            outfile.write("Case #" + str(case + 1) + ": " + "resultado" + "\n")
