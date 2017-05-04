import os

in_file_path = os.path.join(os.path.dirname(__file__), "test1.txt")
out_file_path = os.path.join(os.path.dirname(__file__), "testOutput.txt")

with open(in_file_path, 'r') as infile:
    with open(out_file_path, 'w') as outfile:
        cases = infile.readline()
        # print(cases)
        for case in range(int(cases)):
            print("CASO NUMERO: ", case)
            scores = []
            n_rolls = " ".join(infile.readline().split())
            rolls = (infile.readline().split())  # rolls es una lista
            # print(rolls)
            for i, roll in enumerate(rolls):
                if int(roll) == 10:  # se produce un strike
                    rolls.insert(i + 1, 0)
            print("ROLLS EN BRUTO:", rolls, )
            for i, roll in enumerate(rolls):
                if int(roll) == 10:
                    if rolls[i+2] != 10:
                        bonus = int(rolls[i + 2]) + int(rolls[i + 3])
                        rolls[i] = int(roll) + bonus
                    else:
                        bonus = int(rolls[i+2]) + int(rolls[i+4])
                        rolls[i] = roll + bonus

            print("ROLLS MODIFICADO: ", rolls)

            for i, roll in enumerate(rolls):
                if int(roll) > 10:
                    del (rolls[i + 1])
            print("ROLLS SIN CEROS", rolls)

            for i, roll in enumerate(rolls):
                if i < len(rolls) - 1:
                    if int(roll) < 10:
                        roll_1 = int(rolls[i])
                        roll_2 = int(rolls[i + 1])
                        frame = roll_1 + roll_2
                        if frame == 10:
                            print("SPARE")
                            rolls[i] = frame + int(rolls[i + 2])
            print("ROLLS CON SPARES: ", rolls)

            for i, roll in enumerate(rolls):
                if i < len(rolls) - 1 and i % 2 == 0:
                    if i == len(rolls)-3 and roll == 10:
                        scores.append(roll)
                        scores.append(rolls[i+1])
                        scores.append(rolls[i+2])
                    if int(roll) > 10:
                        rolls.insert(i+1, 0)
                        scores.append(roll)
                    else:
                        roll_1 = int(rolls[i])
                        roll_2 = int(rolls[i + 1])
                        frame = roll_1 + roll_2
                        scores.append(frame)

            print("SCOREBOARD", scores)
            for i, score in enumerate(scores):
                if i != 0:
                    scores[i] += scores[i-1]
            print("SCOREBOARD", scores, "\n")
