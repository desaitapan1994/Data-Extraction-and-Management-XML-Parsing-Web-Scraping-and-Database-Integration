import requests
from bs4 import BeautifulSoup
import csv
presidents = []
ahrefs = []
url = 'https://www.infoplease.com/homework-help/history/collected-state-union-addresses-us-presidents'
response = requests.get(url)
soup = BeautifulSoup(response.content,'lxml')
links = soup.find_all('dt')
for link in links:
    presidents.append(link.span.a.text)
    ahrefs.append(link.span.a.get('href'))
with open('usaSpeechDetails.csv','w',newline='') as file:
    writer = csv.writer(file)
    fileNumber=0
    for href in ahrefs:
        url = "https://www.infoplease.com"+href
        response = requests.get(url)
        soup = BeautifulSoup(response.content,'lxml')
        link = presidents[fileNumber]
        dateIndex = link.find('(')
        fileNumber += 1
        if dateIndex == -1:
            continue
        nameOfPresident=link[0:dateIndex]
        dateOfAddress=link[dateIndex+1:-1]
        print(nameOfPresident,dateOfAddress)
        header = soup.find('div',{'class':'navheader'})
        if(header):
            textofAddress = header.text
        ps = soup.find("div",{'class':'article'})
        if(ps is None):
            continue
        pss= ps.find_all("p")
        fileContent=''
        for i in range(len(pss)):
            if i==0:
                if(textofAddress==''):
                    textofAddress = pss[i].text[0:-2]
            ss = pss[i].text
            fileContent = fileContent + ss
        fileName = '.\Lab3\InfoUnionAddress_'+str(fileNumber)+'.txt'
        f = open(fileName,"w")
        f.write(fileContent)
        f.close()
        writer.writerow([nameOfPresident,dateOfAddress,url,fileName,textofAddress])
        