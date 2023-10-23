# Pandas Memory Usage


Why does reading a csv use double the memory of the df?


```python
import pandas as pd
import tracemalloc

tracemalloc.start()

with open("data.txt", 'w') as f:
    f.write('x\n')
    for i in range(1000000):
        f.write(f'{i}\n')

current, peak = tracemalloc.get_traced_memory()
print(f"Current {int(current / 10 ** 6)} MB Peak {int(peak / 10 ** 6)} MB")

df = pd.read_csv('data.txt', dtype='int32')
current, peak = tracemalloc.get_traced_memory()
print(f"Current {int(current / 10 ** 6)} MB Peak {int(peak / 10 ** 6)} MB")
```

Output
```text
Current 0 MB Peak 0 MB
Current 4 MB Peak 8 MB
```
