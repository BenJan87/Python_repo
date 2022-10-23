import argparse, re, os

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
    if end_char in "\\*+?.|[]\{\}^$":
        pattern = rf"\{end_char}$"
    else:
        pattern = rf"{end_char}$"

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
    os.remove("tmp_file.txt")
    


def spaces(file):
    pass


def leading_spaces(file):
    pass


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--files", help="input file", required=True, nargs='+')
    parser.add_argument('-l', '--leading-spaces', help='skip the spaces except the leading spaces',
                        nargs='+')
    parser.add_argument('-s', '--spaces', help='skipt all of the spaces', nargs='+')
    parser.add_argument('-c', '--concat', help='converting the continutation of code into one line (ends with "\\")',
                        default="\\")
    

    try:
        args = parser.parse_args()
        
    except:
        print("Specify file names and check the flags (-h or --help for descriptions)")

    files = args.files

    for file in files:
        if not concation(file, args.concat[0]):
            pass
    