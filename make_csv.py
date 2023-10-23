

with open("data.txt", 'w') as f:
    f.write('x\n')
    for i in range(1000000):
        f.write(f'{i}\n')
