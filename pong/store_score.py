from settings import *
import os
import fileinput

def update_score(id, score):
    global n
    global data
    n = 0
    data = str(id) + ',' + str(score)
    if score == 1:
        f = open(os.path.dirname(os.path.abspath(__file__)) + "/back/scores.txt", "a")
        f.writelines(data + "\n")
        f.close()
    else:
        replace_in_file(os.path.dirname
                        (os.path.abspath(__file__)) + "/back/scores.txt", str(id)
                          + ',' + str(score-1),
                          data)

def replace_in_file(file_path, search_text, new_text):
    with fileinput.input(file_path, inplace=True) as file:
        for line in file:
            new_line = line.replace(search_text, new_text)
            print(new_line, end='')
