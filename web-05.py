import urllib.request

ud = urllib.request.urlopen("http://webhacking.kr/challenge/web/web-05/mem/login.php")
binary = ud.read()
ud.close()
