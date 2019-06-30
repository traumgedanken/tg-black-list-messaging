import time

start = time.time()
while time.time() - start < 10:
    print(start)
    time.sleep(0.1)
    # print(int(10 * (time.time() - start)) / 10)
    # time.sleep(0.1)
