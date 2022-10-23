from errno import ESTALE
import os
import re

#how to find with re end of the line /? and
def printing_file(file):
    file = open(file, "r")
    for el in file.readlines():
        print(el, end="")
    file.close()

def concation(given_file, end_char):
    tmp_file = open('tmp_file.txt', 'w+')

    try:
        given_file = open(given_file, 'r')
    except:
        print(f"File {given_file} doesn't exist")
        tmp_file.close()
        os.remove("tmp_file.txt")
        return False

    
    lines = given_file.readlines()
    tmp_string = ""
    if end_char == "\\":
        pattern = rf"\{end_char}$"
    else:
        pattern = rf"\{end_char}$"

    print(pattern)

    for line in lines:
        last = lines[-1]
        if line is not last:
            line = line[:-1]
        if re.search(pattern, line):
            tmp_string += line[:-1]
        else:
            tmp_string += line
            if line is not last:
                tmp_file.write(tmp_string+"\n")
            else:
                tmp_file.write(tmp_string)
            tmp_string = ""
    
    tmp_file.close()
    printing_file("tmp_file.txt")
    tmp_file.close()
    
if __name__ == "__main__":
    concation("C:\\Users\\benja\\OneDrive\\Pulpit\\Studia_AGH\\git_repos\\Python_repo\\AGH_course_exercises\\III_sem\\26.10.2022\\file.txt",
             "|")