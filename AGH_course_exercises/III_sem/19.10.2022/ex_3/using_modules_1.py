from sys import argv

if argv[1] == "--lista":
    from lista import wypisz, zapisz
    wypisz(zapisz(argv[2:]))

elif argv[1] == "--slownik":
    from slownik import wypisz, zapisz
    wypisz(zapisz({}, argv[2:]))

else:
    print("Not correct flag -> exiting")
    exit()