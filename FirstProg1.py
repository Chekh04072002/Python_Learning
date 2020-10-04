def CountSort(A):
    list = [0] * 101
    for count in A:
        list[count] += 1
    for count1 in range(len(list)):
        if list[count1] == 0:
            continue
        print((str(count1) + ' ') * list[count1], end=' ')


myList = list(map(int, input().split()))
CountSort(myList)

Дан список из N (N≤2*10⁵) элементов, которые принимают целые значения от 0 до 100 (100 включая).

Отсортируйте этот список в порядке неубывания элементов. Выведите полученный список.

Решение оформите в виде функции CountSort(A), которая модифицирует передаваемый ей список. Использовать встроенные функции сортировки нельзя.