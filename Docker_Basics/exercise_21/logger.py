import time

count = 1

while True:
    print(f"Log message {count}", flush=True)
    count += 1
    time.sleep(2)
