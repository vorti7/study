import csv
import requests
from bs4 import BeautifulSoup

addr = 'http://en.wikipedia.org/wiki/Comparison_of_text_editors'
resp = requests.get(addr)


if(resp.status_code==requests.codes.ok):
    html = resp.text
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.findAll('table',{'class':'wikitable'})
    for i in range(len(table)):
        rows = table[i].findAll('tr')
        csvFile = open('editors'+ str(i) +'.csv','wt+')
        writer = csv.writer(csvFile)
        try:
            for row in rows:
                csvRow = []
                for cell in row.findAll(['td', 'th']):
                    csvRow.append(cell.get_text())
                writer.writerow(csvRow)
        finally:
            csvFile.close()
else:
    print(resp.status_code,'접속실패')
