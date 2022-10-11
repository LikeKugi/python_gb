# Дано число N. Заполните список длиной N
# элементами 1, -3, 9, -27, 81, -243

n = int(input())

numbers = [(-3)**i for i in range(n)]
print(numbers)