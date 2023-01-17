import time
import sys
print("Loading...\n")
for i in range(5):
    print("[", i*"*", (5 - i)*" ", "] ", i * 20, "%")
    time.sleep(1)
    sys.stdout.write('\x1b[1A')
    sys.stdout.write('\x1b[2K')