import signal
def my_exit():
    print("exiting")
    exit()
while True:
    handler = signal.signal(signal.SIGTERM, my_exit())
