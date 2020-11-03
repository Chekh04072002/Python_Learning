fin = open('input.txt', 'r')
fout = open('output.txt', 'w')
myList = []
dictList = {}
st = fin.readlines()
for word in st:
    myList.extend(word.lower().split())

for word in myList:
    if word in dictList:
        dictList[word] += 1
    elif word not in dictList:
        dictList[word] = 1

max = (0, 0)
for word in dictList:
    if dictList[word] > max[0]:
        max = (dictList[word], word)
    if dictList[word] == max[0]:
        if word < max[1]:
            max = (dictList[word], word)
print(max[1], max[0])


Недавно мы считали для каждого слова количество его вхождений в строку. Но на все слова может быть не так интересно смотреть, как, например, на наиболее часто используемые.

Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки) и выводит самое частое слово в этом тексте и через пробел то, сколько раз оно встретилось. Если таких слов несколько, вывести лексикографически первое (можно использовать оператор < для строк).

В качестве ответа укажите вывод программы, а не саму программу.

Слова, написанные в разных регистрах, считаются одинаковыми.