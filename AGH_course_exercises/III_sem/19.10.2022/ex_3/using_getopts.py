import sys, getopt

def script_getopt():
    command_args = sys.argv[1:]
    short_options = "m:"
    long_options = ["moduł="]

    optlist, args = getopt.getopt(command_args, short_options, long_options)
    module = optlist[0][1]


    if module == "lista":
        from lista import wypisz, zapisz
        
        wypisz(zapisz([], sys.argv[2:]))

    elif module == "slownik":
        from slownik import wypisz, zapisz
        wypisz(zapisz({}, sys.argv[2:]))

    else:
        print("Not correct flag -> exiting")
        exit()

if __name__ == "__main__":
    script_getopt()