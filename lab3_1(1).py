# -*- coding: utf-8 -*-
import csv
import requests
import xml.etree.ElementTree as ET

def save2csv(child,type,bookId,price=None):
    with open('book.csv','a',newline='') as file:
        writer = csv.writer(file)
        publisher=''
        title=''
        year=''
        for item in child:
            if(item.tag=='publisher'):
                publisher = item.text;
            if(item.tag=='year'):
                year = item.text
            if(item.tag=='title'):
                title=item.text
            if(item.tag=='author'):
                with open('author.csv','a',newline='') as authorFile:
                    authorWriter = csv.writer(authorFile)
                    if(len(list(item))==0):
                        authorWriter.writerow([bookId,item.text])
                    if(len(list(item))==2):
                        if(item[0].tag=='first-name' and item[1].tag=='last-name'):
                            authorName = item[0].text+item[1].text
                            authorWriter.writerow([bookId,authorName])
                        elif(item[0].tag=='name'):
                            authorName = item[0].text
                            if(item[1].tag=='address'):
                                authorAddress = item[1][0].text +item[1][1].text
                                authorWriter.writerow([bookId,authorName,authorAddress])
                    if(len(list(item))==3):
                        
                        authorName = item[0].text+item[1].text
                        authorAddress= item[2][0].text + item[2][1].text
                        authorWriter.writerow([bookId,authorName,authorAddress])
                       
        writer.writerow([bookId,publisher,title,year,price,type])
                
    


def parseXML(xmlfile):
    tree = ET.parse(xmlfile)
    items = []
    root = tree.getroot()
    bookId=0
    for items in root:
        
        for child in items:
            bookId += 1
            
            if child.tag == 'book':
                if(child.attrib):
                    save2csv(child,'book',bookId,child.attrib['price'])
                else:
                    save2csv(child,'book',bookId)
                
            else:
                save2csv(child,'paper',bookId)


xmlItems = parseXML('file.xml')
