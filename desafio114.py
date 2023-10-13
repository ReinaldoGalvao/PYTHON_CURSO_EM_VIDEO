'''
Teste se o site www.pudim.com.br está online
'''
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br/')
except urllib.error.URLErro:
    print('Deu erro')
else:
    print('Tudo ok')