import time
import numpy as np
import matplotlib as plt
def median(numbers):
    min_h = None
    min_value = float('inf')
    for h in numbers:
        total_abs_loss = 0
        for x in numbers:
            total_abs_loss += abs(x - h)
        if total_abs_loss < min_value:
            min_value = total_abs_loss
        min_h = h
    return min_h

def time_median(data):
    start = time.time()
    median(data)
    return time.time() - start

def avg(n, trial):
    times = []
    for i in range(trial):
        data = np.random.randint(0, 10000, n)
        tmed = time_median(data)
        times.append(tmed)
    return sum(times)/trial

n = [100, 400, 700, 1000, 1300, 1600, 1900]
times = [avg(i, 20) for i in n]

print(times)