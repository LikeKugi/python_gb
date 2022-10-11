n = int(input())

for i in range(1, int(n ** 0.5)):
    if n % i == 0:
        print(i, ('even', 'odd')[i % 2 == 0])
        print(n // i, ('even', 'odd')[(n // i) % 2 == 0])
