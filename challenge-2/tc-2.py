import os

in_file_path = os.path.join(os.path.dirname(__file__), "submitInput.txt")
out_file_path = os.path.join(os.path.dirname(__file__), "testOutput.txt")

with open(in_file_path, 'r') as infile:
    with open(out_file_path, 'w') as outfile:
        cases = infile.readline()

        for case in range(int(cases)):
            score = 0
            scores = []
            n_rolls = " ".join(infile.readline().split())
            rolls = list(map(int, (infile.readline().split())))
            frame = 0
            for i in range(10):
                if rolls[frame] == 10:
                    score += 10 + rolls[frame + 1] + rolls[frame + 2]
                    frame += 1
                elif rolls[frame] + rolls[frame + 1] == 10:
                    score += 10 + rolls[frame + 2]
                    frame += 2
                else:
                    score += rolls[frame] + rolls[frame + 1]
                    frame += 2

                scores.append(score)

            outfile.write("Case #" + str(case + 1) + ": " + ' '.join(str(score) for score in scores) + "\n")
