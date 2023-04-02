import time

loading_lines = ["Loading...", "Please wait...", "Processing..."]

for line in loading_lines:
    print(line, end="", flush=True)
    time.sleep(1)
    print("\r" + " " * len(line), end="", flush=True)