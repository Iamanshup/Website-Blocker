import time
from datetime import datetime as dt

website_list = ['www.facebook.com', 'facebook.com', 'www.twitter.com', 'twitter.com']
redirect = '127.0.0.1'
hosts_path = r'C:\Windows\System32\drivers\etc\hosts'

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 9) <= dt.now() <= dt(dt.now().year, dt.now().month, dt.now().day, 17):
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + ' ' + website + '\n')
    else:
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()

    time.sleep(5)
