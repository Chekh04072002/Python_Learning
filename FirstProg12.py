setList1 = set(map(int, input().split()))
setList2 = set(map(int, input().split()))
myList1 = list(setList1)
myList11 = []
myList22 = []
myList2 = list(setList2)
myList1.sort()
myList2.sort()
for i in range(myList1[0], myList1[1] + 1):
    myList11.append(i)
for q in range(myList2[0], myList2[1] + 1):
    myList22.append(q)
setList1 = set(myList11)
setList2 = set(myList22)
print(len(setList1 & setList2))


На Новом проспекте для разгрузки было решено пустить два новых автобусных маршрута на разных участках проспекта. Известны конечные остановки каждого из автобусов. Определите количество остановок, на которых можно пересесть с одного автобуса на другой.

Формат ввода

Вводятся четыре числа, не превосходящие 100, задающие номера конечных остановок. Сначала для первого, потом второго автобуса (см. примеры и рисунок).

Формат вывода

Ваша программа должна выводить одно число – искомое количество остановок.