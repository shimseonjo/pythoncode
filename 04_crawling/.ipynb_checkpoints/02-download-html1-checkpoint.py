import urllib.request

url='https://www.google.com/'

mem=urllib.request.urlopen(url).read()
print(mem.decode('utf-8'))