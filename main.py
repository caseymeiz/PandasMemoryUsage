import pandas as pd
import tracemalloc

with open("data.txt", 'w') as f:
    f.write('x\n')
    f.write('\n'.join(str(i) for i in range(1000000)))

tracemalloc.start()

current, peak = tracemalloc.get_traced_memory()
print(f"Current {int(current / 10 ** 6)} MB Peak {int(peak / 10 ** 6)} MB")

df = pd.read_csv('data.txt', dtype='int32')
current, peak = tracemalloc.get_traced_memory()
print(f"Current {int(current / 10 ** 6)} MB Peak {int(peak / 10 ** 6)} MB")
