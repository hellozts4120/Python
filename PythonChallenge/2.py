import urllib2
content = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/ocr.html').read()
new = ""
for i in content:
    if (i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Z'):
        new += i
print new