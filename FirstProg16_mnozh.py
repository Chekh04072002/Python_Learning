fin = open('input.txt', 'r', encoding='utf-8')
fout = open('output.txt', 'w', encoding='utf-8')
myList = []
dictList = {}
tupleList = []
lList = []
count = 0

for phraz in fin:
    myList.extend(phraz.split('\n'))
    count += 1

for i in range(0, len(myList), 2):
    if myList[i] in dictList:
        dictList[myList[i]] += 1
    else:
        dictList[myList[i]] = 1

for w in dictList:
    tupleList.append((dictList[w], w))

for e in range(len(tupleList) - 1, 0, -1):
    if tupleList[e] < tupleList[e - 1]:
        a = tupleList[e]
        tupleList[e] = tupleList[e - 1]
        tupleList[e - 1] = a

kand1 = tupleList[-1]
kand2 = tupleList[-2]

if (kand1[0] / count) * 100 > 50:
    print(kand1[1])
else:
    print(kand1[1], kand2[1], sep='\n')


В выборах Президента Российской Федерации побеждает кандидат, набравший свыше половины числа голосов избирателей. Если такого кандидата нет, то во второй тур выборов выходят два кандидата, набравших наибольшее число голосов.

Формат ввода

Каждая строка входного файла содержит имя кандидата, за которого отдал голос один избиратель. Известно, что общее число кандидатов не превосходит 20, но в отличии от предыдущих задач список кандидатов явно не задан. Читайте данные из файла input.txt с указанием кодировки utf8.

Формат вывода

Если есть кандидат, набравший более 50% голосов, программа должна вывести его имя. Если такого кандидата нет, программа должна вывести имя кандидата, занявшего первое место, затем имя кандидата, занявшего второе место. Выводите данные в файл output.txt с указанием кодировки utf8.