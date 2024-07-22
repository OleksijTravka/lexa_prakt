import requests
import json

# account_id = input("Enter player id: ")
account_id = "61783959"

y = requests.get('https://api.opendota.com/api/players/' + account_id + '/recentMatches')
dota_hero_stats = requests.get('https://api.opendota.com/api/heroStats')
d = json.loads(dota_hero_stats.text)

print(y.text)

slovar = {}
for hirod in d:
    slovar[(str(hirod["id"]))] = hirod["localized_name"]

for kluxh in slovar.keys():
    print(kluxh +"  "+slovar[kluxh])

for dota_hero_stats in slovar:







'''
    Вытянуть прошлые матчи из recentMatches
    Сохранить список всех геров в словарь из heroStats
    Взять оттуда нужную инфу
    В инфе про матч конвертировать айди героя в имя героя
    244921964
'''