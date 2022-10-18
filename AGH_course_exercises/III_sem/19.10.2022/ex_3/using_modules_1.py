from sys import argv

def script_module(argv):
    if argv[1] == "--lista":
        from lista import wypisz, zapisz
        wypisz(zapisz([], argv[2:]))

    elif argv[1] == "--slownik":
        from slownik import wypisz, zapisz
        wypisz(zapisz({}, argv[2:]))

    else:
        print("Not correct flag -> exiting")
        exit()

if __name__ == "__main__":
    script_module(argv)