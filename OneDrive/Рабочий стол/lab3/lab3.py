n = int(input())
sum = 0
for i in range(1, n + 1):
    sum += i
# можно доказать формулу:
# sum == n * (n + 1) // 2
# но мы посчитаем это значение циклом
for i in range(n - 1):
    sum -= int(input())
print(sum)