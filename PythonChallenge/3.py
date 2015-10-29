import re
import urllib2
content = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/equality.html').read()
new = ""
tran =  re.compile(r'[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]', re.S)
print tran.findall(content)

#next:http://www.pythonchallenge.com/pc/def/linkedlist.php