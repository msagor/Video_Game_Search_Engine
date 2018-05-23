from urllib2 import urlopen
import json
import codecs
import re

response = urlopen("http://192.168.56.1:8983/solr/task3/select?q=title:*&rows=25000&wt=json")
#response = urlopen("http://192.168.56.1:8983/solr/task3/select?q=genre:action&rows=25000&wt=json")
#response = urlopen("http://192.168.56.1:8983/solr/task3/select?q=genre:adventure&rows=25000&wt=json")
#response = urlopen("http://192.168.56.1:8983/solr/task3/select?q=title:need%20for%20speed&fq=genre:racing&fq=platform:pc&rows=25000&wt=json")
str_response = response.read().decode('utf-8')
obj = json.loads(str_response)
for x in range (0, obj["response"]["numFound"]):
	print(str(obj["response"]["docs"][x]["title"][0].encode('utf-8')))