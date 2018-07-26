# import urllib.request
# import json
# req = urllib.request.urlopen("https://www.alimi.or.kr/dataview/a/waterStatus/selectYsNationalAggregate.do")
# opener = urllib.request.build_opener()
# f = opener.open(req)
# json = json.loads(f.read())
# print(json)
import requests
import json
url = 'https://www.alimi.or.kr/dataview/a/waterStatus/selectYsNationalAggregate.do'

data = requests.get(url).text
parsed_data = json.loads(data)
