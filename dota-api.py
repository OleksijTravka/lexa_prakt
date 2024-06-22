import requests

account_id = input("Enter player id: ")
# 61783959

y = requests.get('https://api.opendota.com/api/players/' + account_id + '/recentMatches')
dota_hero_stats = requests.get('https://api.opendota.com/api/heroStats')


print(y.text)

'''
    Вытянуть прошлые матчи из recentMatches
    Сохранить список всех геров в словарь из heroStats
    Взять оттуда нужную инфу
    В инфе про матч конвертировать айди героя в имя героя
'''