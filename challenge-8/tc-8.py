import os

in_file_path = os.path.join(os.path.dirname(__file__), "submitInput.txt")
out_file_path = os.path.join(os.path.dirname(__file__), "testOutput.txt")


def transform(caracteres):
    try:
        return '{0:1x}'.format(int(caracteres))
    except:
        return "N/A"


with open(in_file_path, 'r', encoding='utf-16-le') as infile:
    with open(out_file_path, 'w', encoding='utf-16-le') as outfile:
        for i, line in enumerate(infile.readlines()[1:]):
            print(
                "Case #" + str(i + 1) + ": " + transform(line.strip()))
