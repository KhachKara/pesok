import urllib.request

html = urllib.request.urlopen('http://www.mail.ru').read()
print(html)
