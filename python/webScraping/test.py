# from urllib.request import urlopen
# response = urlopen("http://www.naver.com")
# from bs4 import BeautifulSoup
import json
jsonString="""[
{
    "id":12345,
    "title":"This is a title",
    "content":"This is contents.",
    "score": 90
},
{
    "id":54321,
    "title":"Title is this",
    "content":"Contents are these.",
    "score": 10
}
]"""
jsonObj = json.loads(jsonString)
