fin = open('input.txt', 'r', encoding='utf-8')
lines = fin.readlines()
myList = []
dictList = {}
for line in lines:
    myList.extend(line.split())

for word in myList:

    if word in dictList:
        dictList[word] += 1
    else:
        dictList[word] = 0
    print(dictList[word], end=' ')



Во входном файле (вы можете читать данные из файла input.txt) записан текст. Словом считается последовательность непробельных подряд идущих символов. Слова разделены одним или большим числом пробелов или символами конца строки. Для каждого слова из этого текста подсчитайте, сколько раз оно встречалось в этом тексте ранее.

Формат ввода

Вводится текст.

Формат вывода

Выведите ответ на задачу.