import json
import urllib3


class OpenWeatherMap_api():

    def __init__(self, country_code, zip_code):
        req = urllib3.PoolManager()
        header = {'User-agent': 'Python Test'}
        appid = 'e34f2cbecd9493dcf3a91b6b601ed2f9'
        url = 'api.openweathermap.org/data/2.5/forecast/hourly?zip=' + zip_code +','+country_code + '&appid=' + appid
        print(url)
