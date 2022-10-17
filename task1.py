# 1.Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

from random import randint

estimates = [randint(1, 5) for _ in range(
    int(input('\nEnter the number of estimates:\t')))]

changed_estimates = list(
    map(lambda x: x if x < 4 else randint(1, 3), estimates))
print(*estimates)
print(*changed_estimates)
