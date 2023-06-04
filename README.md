# Data-Extraction-and-Management-XML-Parsing-Web-Scraping-and-Database-Integration

The script parses an XML file containing book and paper information, extracting relevant data and saving it to a CSV file.Then it performs web scraping on a webpage to extract State of the Union addresses of US Presidents, saving the speech details to a CSV file and creating separate text files for each speech.This code connects to a SQL Server database and creates tables for books and authors if they don't exist. Later It inserts data from CSV files into the respective tables, ensuring the changes are committed to the database.

Setup and process
1.	Install sql server express edition
2.	Install sql server management studio
3.	Install Python 3.x
4.	used packages in python
a.	pyodbc  - for sql server odbc connection
b.	csv – to read or write csv files using python
c.	requests – to connect with internet for data 
d.	etree – to read xml file
5.	install anaconda ide for the development
The execution to generate the output files in structured any text file format in(csv,tsv)
1.	I developed 3 python file named
a.	Lab1.py – this file is used to read data from xml file and stores it into two files named “book.csv” and “author.csv”. the author csv also contains the bookid as a foreign key because a book can have more than one author. So I created two separate csv file one for book details and other for author detais
b.	Lab2.py – this file is used to read data from website and stores it into csv file named “usaSpeechDetails.csv”
c.	Lab3.py – this file is used to create table and store csv files to tables.

