import requests
response = requests.get('https://public.karat.io/content/test/test_log.txt')
count = 0
ar = response.text.split('\n')
for i in ar:
 if 'Block' in i:
    count = count+1
print(count)


import urllib.request
import pdb;pdb.set_trace()
webUrl=urllib.request.urlopen('https://public.karat.io/content/test/test_log.txt')


fdsds