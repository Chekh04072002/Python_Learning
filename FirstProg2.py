fin = open('input.txt', 'r', encoding='utf-8')
fout = open('output.txt', 'w', encoding='utf-8')
i = 0
max9 = 0
max10 = 0
max11 = 0
myList = []
newList = []
for line in fin:
    myList.extend(line.split('\n'))
while(i < len(myList)):
    if myList[i] == '':
        del myList[i]
    i += 1
for w in range(len(myList)):
    if myList[w][-4] == '9':
        if max9 < int(myList[w][-2:]):
            max9 = int(myList[w][-2:])
for e in range(len(myList)):
    if myList[e][-5:-3] == '10':
        if max10 < int(myList[e][-2:]):
            max10 = myList[e][-2:]
for r in range(len(myList)):
    if myList[r][-5:-3] == '11':
        if max11 < int(myList[r][-2:]):
            max11 = myList[r][-2:]
print(max9, max10, max11)


В олимпиаде по информатике принимало участие несколько человек. Победителем олимпиады становится человек, набравший больше всех баллов. Победители определяются независимо по каждому классу. Определите количество баллов, которое набрал победитель в каждом классе. Гарантируется, что в каждом классе был хотя бы один участник.

Формат ввода

Информация о результатах олимпиады записана в файле, каждая строка которого имеет вид:фамилия имя класс балл.

Фамилия и имя — текстовые строки, не содержащие пробелов. Класс - одно из трех чисел 9, 10, 11. Балл - целое число от 0 до 100.

В этой задаче файл необходимо считывать построчно, не сохраняя содержимое файла в памяти целиком.

Формат вывода

Выведите три числа: баллы победителя олимпиады по 9 классу, по 10 классу, по 11 классу. Входной файл в кодировке utf-8 (В Python используйте open('input.txt', 'r', encoding='utf-8')).