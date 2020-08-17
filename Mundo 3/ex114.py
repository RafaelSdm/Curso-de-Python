import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print("no momento o site nao esta acessivel")
else:
    print("site encontrado")
