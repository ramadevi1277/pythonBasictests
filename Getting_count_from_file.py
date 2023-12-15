import requests
response = requests.get('https://public.karat.io/content/test/test_log.txt')
count = 0
ar = response.text.split('\n')
for i in ar:
 if 'Block' in i:
    count = count+1
print(count)


import urllib.request
webUrl=urllib.request.urlopen('https://public.karat.io/content/test/test_log.txt')


def get_books_and_pages_count():
    response = requests.get("https://public.karat.io/content/test/test_file.txt")
    list_of_lines= response.text.split('\n')
    pages_count = 0
    for line in list_of_lines:
        #import pdb;pdb.set_trace()
        pages_count = pages_count + int(line.split(',')[3])
    print("total_pages", pages_count)
    print("Total_books", len(list_of_lines))
    print(list_of_lines)


get_books_and_pages_count()