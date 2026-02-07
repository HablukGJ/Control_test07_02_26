import time
import random
import numpy as np

def benchmark(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        global lst
        time1 = time.time()
        func(lst)
        time2 = time.time()
        print(f'Time{time2-time1}')
        print(f"Функция: {func.__name__}")

        return result

    return wrapper

# Task 1

# @benchmark
# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n - 1):
#         swapped = False
#         for j in range(0, n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#                 swapped = True
#         if not swapped:
#             break
#     return arr
#
# @benchmark
# def sort(arr):
#     return sorted(arr)
#
# lst = [random.randint(0, 100000) for _ in range(10000)]
# bubble_sort(lst)
# sort(lst)
# Встроенный sort работает гораздо быстрее, чем bubble_sort

# Task 2

# n = int(input("Введите размер матрицы: "))
# step = int(input("Введите сдвиг матрицы (отрицательный для сдвига влево): "))
#
# matrix = [[random.randint(0, 15) for _ in range(n)] for __ in range(n)]
#
# def shift_matrix(matrix, k):
#     k = k % n
#     new = []
#
#     for row in matrix:
#         new_row = row[n-k:] + row[:n-k]
#         new.append(new_row)
#     return new
#
# for row in matrix:
#     for element in row:
#         print(element, end='\t')#Ставит в конце таб
#     print()
#
# for row in shift_matrix(matrix, step):
#     for element in row:
#         print(element, end='\t')#Ставит в конце таб
#     print()

# Task 3

# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#
#     pivot = arr[len(arr) // 2]
#     left = [x for x in arr if x < pivot]
#     middle = [x for x in arr if x == pivot]
#     right = [x for x in arr if x > pivot]
#
#     return quick_sort(left) + middle + quick_sort(right)
#
# n = int(input("Размер матрицы: "))
# matrix = np.array([[random.randint(0, 15) for _ in range(n)] for __ in range(n)])
#
# for row in matrix:
#     for element in row:
#         print(element, end='\t')#Ставит в конце таб
#     print()
#
# transposed = matrix.T
# new_transposed = []
# for row in transposed:
#     new_transposed.append(quick_sort(row))
#
# for row in np.array(new_transposed).T:
#     for element in row:
#         print(element, end='\t')#Ставит в конце таб
#     print()

# Task 4

# @benchmark
# def find_max_linear(arr):
#     max_val = arr[0]
#     for num in arr[1:]:
#         if num > max_val:
#             max_val = num
#     return max_val
#
# @benchmark
# def find_max_bubble(arr):
#     n = len(arr)
#     for i in range(n - 1):
#         swapped = False
#         for j in range(0, n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#                 swapped = True
#         if not swapped:
#             break
#     return arr[len(arr) - 1]
#
# lst = [random.randint(0, 10000) for _ in range(10000)]
# print(find_max_linear(lst))
# print(find_max_bubble(lst))

# Итак, первый способ работает гораздо эффективнее (даже замерить не смог, всегда 0.0)
# bubble_sort_max: 0.0015 - время затраченное на выполнение
# linear_max: 0.0