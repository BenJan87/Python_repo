def sum(arg1, arg2):
#if "j" occurs -> it means 1j (complex)
        def check_var(str_num):
                if "j" in str_num:
                        return complex(str_num)
                if "." in str_num:
                        return float(str_num)
                return int(str_num)

        arg1, arg2 = check_var(str(arg1)), check_var(str(arg2))
        return arg1 + arg2


if __name__ == "__main__":
    suma = sum(2, 6)
    print(suma)
    print("__name__ = {0}".format(__name__))