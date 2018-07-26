import urlparse
url = 'https://www.alimi.or.kr/dataview/a/waterStatus/selectYsNationalAggregate.do'
parsed = urlparse.urlparse(url)
print urlparse.parse_qs(parsed.query)['def']
