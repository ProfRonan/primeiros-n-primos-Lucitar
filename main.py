n = int(input())

rep = 0
i = 2
while rep < n:
    div = 0
    for i2 in range(2, i):
        if i % i2 == 0:
            div += 1
    if div == 0:
        print(i)
        rep += 1
    i += 1
    