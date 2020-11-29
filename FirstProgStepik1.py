import requests
import sys

fin = open('dataset_24476_3.txt')


for line in fin:
    line = int(line.strip())
    i = line
    url = f'http://numbersapi.com/{i}/math?json'
    res = requests.get(url)
    output = res.json()
    flag = output['found']
    if flag:
        print('Interesting')
    else:
        print('Boring')

В этой задаче вам необходимо воспользоваться API сайта numbersapi.com

Вам дается набор чисел. Для каждого из чисел необходимо узнать, существует ли интересный математический факт об этом числе.

Для каждого числа выведите Interesting, если для числа существует интересный факт, и Boring иначе.
Выводите информацию об интересности чисел в таком же порядке, в каком следуют числа во входном файле.

Пример запроса к интересному числу:
http://numbersapi.com/31/math?json=true

Пример запроса к скучному числу:
http://numbersapi.com/999/math?json=true

Пример входного файла:
31
999
1024
502

﻿Пример выходного файла:
Interesting
Boring
Interesting
Boring






# import requests
#
# url = 'http://api.openweathermap.org/data/2.5/weather'
# city = input('Введите название города: ')
# cityApi = {
#     'q': city,
#     'appid': '2f3d38711cb544e16f85c33b6b22a9c7',
#     'units': 'metric'
# }
# res = requests.get(url, cityApi)
# # print(res.status_code)
# # print(res.headers['Content-Type'])
# output = res.json()
# print(output['main']['temp'])
