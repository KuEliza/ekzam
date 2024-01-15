"""
Кузнецова
Дан двумерный массив целых чисел. Напишите скрипт нахождения строки с минимальной нечетной суммой элементов.
"""

a = [[10, 15, 3],
    [4, 6, 6],
    [7, 8, 9],
    [10, 11, 12]]

def minimSum(a):

    minOddSum = float('inf')
    minRow = None

    for i in a:
        row_sum = sum(i)
        if row_sum % 2 == 1 and row_sum < minOddSum:
            minOddSum = row_sum
            minRow = i

    return minRow


minRow = minimSum(a)

print("Вывод:", minRow)