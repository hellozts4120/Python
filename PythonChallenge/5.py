import pickle
import urllib2
content = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/banner.p').read()
print pickle.load(content)