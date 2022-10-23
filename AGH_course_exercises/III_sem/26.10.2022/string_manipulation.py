import argparse, re, os


def printing_file(file):
    file1 = open(file, "r")
    print(f"\nopening: {file}\n")
    for el in file1.readlines():
        print(el, end="")
    print("\n"+"-"*40)
    file1.close()


def concatenation(given_file, end_char):
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

    last = lines[-1]
    for line in lines:
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
    
    print("After concatenation:\n")
    tmp_file.close()
    printing_file("tmp_file.txt")
    tmp_file.close()
    return True
    

def spaces(file):
    tmp_file = open("tmp_file_spaces.txt", 'w+')
    given_file = open(file, 'r')
    lines = given_file.readlines()
    last = lines[-1]
    
    for line in lines:
        result_string = ""
        result_arr = re.findall(r'^\s+\S+', line)
        if result_arr:
            result_arr += re.findall(r'\S+', line)[1:]
        else:
            result_arr = re.findall(r'\S+', line)

        for only_word in result_arr:
            result_string += only_word
        
        if line is not last:
            tmp_file.write(result_string+"\n")
        else:
            tmp_file.write(result_string)

    print("After removing spaces:\n")
    tmp_file.close()
    printing_file("tmp_file_spaces.txt")
    tmp_file.close()


def leading_spaces(file):
    tmp_file = open('tmp_file_leading.txt', 'w+')
    given_file = open(file, 'r')
    lines = given_file.readlines()
    last = lines[-1]

    for line in lines:
        reg_object = re.search(r'^\s+', line)
        if reg_object:
            new_line = line[reg_object.end():]
        else:
            new_line = line
        
        if line is not last:
            tmp_file.write(new_line)
        else:
            tmp_file.write(new_line) 
            
    print("After removing leading spaces:\n")
    tmp_file.close()
    printing_file("tmp_file_leading.txt")
    tmp_file.close()  


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--files", help="input file",
                        nargs='+', required=True)
    parser.add_argument('-l', '--leading-spaces', help='skip the leading spaces',
                        action='store_true')
    parser.add_argument('-s', '--spaces', help='skip all of the spaces besides leading',
                        action='store_true')
    parser.add_argument('-c', '--concat', help='converting the continutation of code into one line (default ends with "\\")',
                        default="\\")
    
    try:
        args = parser.parse_args()
    except:
        print("Specify file names and check the flags (-h or --help for descriptions)")

    try:
        files = args.files
    except(NameError):
        exit(0)

    basic_file = "tmp_file.txt"

    
    for file in files:
        try:
            if not concatenation(file, args.concat[0]):
                print(f"No such file as {file}\n")
                continue

            if args.leading_spaces:
                leading_spaces(basic_file)
                if args.spaces:
                    spaces("tmp_file_leading.txt")
                    os.rename("tmp_file_spaces.txt", file+"_changed")
                    continue

                os.rename("tmp_file_leading.txt", file+"_changed")
                continue

            if args.spaces:
                spaces(basic_file)
                os.rename("tmp_file_spaces.txt", file+"_changed")
                continue

            os.rename("tmp_file.txt", file+"_changed")
        except(FileExistsError):
            print(f"File with name {file}_changed already exist\nRemove this file than run the script\n")

    for file in [basic_file, "tmp_file_leading.txt", "tmp_file_spaces.txt"]:
        try:
            os.remove(file)
        except:
            pass