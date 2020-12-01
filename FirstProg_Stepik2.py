import requests
import json
import sys

fin = open('dataset_24476_4.txt', 'r')
client_id = '5ddb844243d14a4cdc8b'
client_secret = 'a43e8bc87bebd1ed789ce136933238b0'

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
j = json.loads(r.text)

# достаем токен
token = j["token"]

# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token": token}
# инициируем запрос с заголовком
myList = []
for i in fin:
    myList.extend(i.split())

myList_end = []
for q in myList:
    indicator = q
    r = requests.get(f"https://api.artsy.net/api/artists/{indicator}", headers=headers)
    r.encoding = 'utf-8'
# разбираем ответ сервера
    j = json.loads(r.text)
    myList_end.append((j['sortable_name'], j['birthday']))

myList_end.sort(key=lambda x: (x[1], x[0]))

for i in range(len(myList_end)):
    print(myList_end[i][0])



