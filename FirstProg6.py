fin = open('input.txt', 'r', encoding='utf-8')
fout = open('output.txt', 'w', encoding='utf-8')
myList = []
m9 = []
m10 = []
m11 = []
for line in fin:
    st = line.split()
    myList.extend((st[2], st[3]))
for i in range(len(myList)):
    if int(myList[i]) == 9:
        m9.extend(myList[i + 1: i + 2])
    elif int(myList[i]) == 10:
        m10.extend(myList[i + 1: i + 2])
    if int(myList[i]) == 11:
        m11.extend(myList[i + 1: i + 2])
m9.sort(reverse=True)
m10.sort(reverse=True)
m11.sort(reverse=True)
for q in range(1, len(m9)):
    if m9[0] == m9[q]:
        continue
    else:
        print(m9[q], end=' ')
for w in range(1, len(m10)):
    if m10[0] == m10[w]:
        continue
    else:
        print(m10[w], end=' ')
for e in range(1, len(m11)):
    if m11[0] == m11[e]:
        continue
    else:
        print(m11[e], end=' ')

Зачет проводится отдельно в каждом классе. Победителями олимпиады становятся школьники, которые набрали наибольший балл среди всех участников в данном классе.

Для каждого класса определите максимальный балл, который набрал школьник, не ставший победителем в данном классе.

Формат вывода

Выведите три целых числа.