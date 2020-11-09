import urllib
import urllib.request

try:
    url= urllib.request.urlopen('http://pudim.com.br')
except urllib.error.URLError:
    print('\033[1;31mO site pudim não está disponível no momento :( \033[m')
else:
    print('\033[1;32mO site pudim está disponível!\033[m')
