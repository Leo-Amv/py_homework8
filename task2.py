# Дано натуральное число N и последовательность из N элементов. Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода). Через рекурсию необходимо делать

# Input: 2 -> 3 4
# Output: 4 3

# sequence_of_numbers = [i for i in range(
#     int(input('\nEnter the number of sequence :\t')))]

def reverse_sequence(n):
    if n < 1:
        print()
    else:
        s = input()
        reverse_sequence(n-1)
        print(s, end='\t')


n = int(input('\nEnter the number of sequence :\t'))
reverse_sequence(n)
