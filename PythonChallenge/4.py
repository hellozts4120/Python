import urllib2
import re
linked = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
nothing = "8022"    #first 12345, need to divide by 2 in the term of running
url = linked + nothing
while nothing:
    #global linked,url,nothing
    try:
        response = urllib2.urlopen(url)
        content = response.read()
        tmp = re.findall("[0-9]+", content)
        nothing = ''.join(tmp)
        url = linked + nothing
        print url
    except:
        print url

#end 66831