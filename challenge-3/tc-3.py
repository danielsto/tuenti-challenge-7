import os

in_file_path = os.path.join(os.path.dirname(__file__), "submitInput.txt")
out_file_path = os.path.join(os.path.dirname(__file__), "testOutput.txt")

with open(in_file_path, 'r') as infile:
    with open(out_file_path, 'w') as outfile:
        cases = infile.readline()
        # print("CASOS: ", cases)
        for case in range(int(cases)):
            points = int(infile.readline())
            cards = 1
            while points > 2:
                points = points / 2
                cards += 1
            if points % 2 == 0:
                cards += 1
            outfile.write("Case #" + str(case + 1) + ": " + str(cards) + "\n")
