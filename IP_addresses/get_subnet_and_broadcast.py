# accept mask from 24-30 inclusive
import re


def ip_converter(ip):
    mask = re.search(r'/[0-9]{2}', ip)
    mask = ip[mask.start()+1:mask.end()]

    begining = re.search(r'[0-9]+\.[0-9]+\.[0-9]+\.', ip)
    ending = int(ip[begining.end():-3])

    step = 2**(32-int(mask))
    count = 0
    while count < 255:
        if count + step > ending:
            return [ip[begining.start():begining.end()]+str(count)+"/"+mask, ip[begining.start():begining.end()]+str(count+step-1)+"/"+mask]
        count += step
        



if __name__ == '__main__':
    while True:
        try:
            for el in ip_converter(input('Give me an ip address (decimal): ')):
                print(el)
        except(EOFError):
            exit(0)
        except:
            print('Give proper value')
