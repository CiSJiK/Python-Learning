import time

start = time.perf_counter() # time.clock() 대신 사용. 사유: 3.7 이후로 Deprecated

count = 0

for i in range(1000000):
    count += 1

end = time.perf_counter()
print(end - start)