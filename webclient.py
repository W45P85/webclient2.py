# Client nach HTTP Konzept

import urllib.request

fhand = urllib.request.urlopen('https://127.0.0.1:9000/daniel.txt')
for line in fhand:
    print(line.decode().strip())
