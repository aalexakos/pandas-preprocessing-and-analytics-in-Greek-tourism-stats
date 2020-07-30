import pandas as pd
import mysql.connector
from get_data import get_most_visits_per_country, get_total_arrivals, arrivals_by_means_of_transport, get_tourists_per_trimester

#all the data that are being uploaded below come from get_data.py's functions that are imported above

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Bilbo83os",
  database="elstat"
)
#uploading total arrivals to database
def total_arrivals_mysql():
  mycursor = mydb.cursor()
  mycursor.execute("CREATE TABLE IF NOT EXISTS total_arrivals (year VARCHAR(255),arrivals INT (10));")
  years=['2011','2012','2013','2014','total']

  sql = "INSERT INTO total_arrivals (year,arrivals) VALUES (%s, %s);"
  for elem in zip(years, get_total_arrivals()):
    mycursor.execute(sql, elem)
    mydb.commit()

#uploading most visited tourists per country
def countries_to_mysql():
  mycursor = mydb.cursor()
  mycursor.execute("CREATE TABLE IF NOT EXISTS countries (country VARCHAR(255),no INT (10));")

  sql = "INSERT INTO countries (country, no) VALUES (%s, %s);"
  mycursor.executemany(sql, get_most_visits_per_country())
  mydb.commit()
  mycursor.execute("SELECT * FROM countries;")
  for x in mycursor:
    print (x)

#means of transport statistics upload to mysql server
def mot_to_mysql():
  mycursor = mydb.cursor()
  mycursor.execute("CREATE TABLE IF NOT EXISTS means_of_transport (means VARCHAR(255), no INT (10));")
  newdict=arrivals_by_means_of_transport()
  means=list(newdict.keys())
  number=list(newdict.values())
  sql='INSERT INTO `means_of_transport` (`means`,`no`) values (%s,%s);'
  for elem in zip(means, number):
    mycursor.execute(sql, elem)
    mydb.commit()
  
mot_to_mysql()
#uploading tourists per trimester
def tourism_per_trimester():
  mycursor = mydb.cursor()
  mycursor.execute("CREATE TABLE IF NOT EXISTS trimesters (trimester VARCHAR(255), no INT(12) );")
  varlist=get_tourists_per_trimester()
  dates=[ ("2011a"),("2011b"),("2011c"),("2011d"),
                          ("2012a"),("2012b"),("2012c"),("2012d"),("2013a"),("2013b"),("2013c"),("2013d"),
                          ("2014a"),("2014b"),("2014c"),("2014d")]
  sql='INSERT INTO `trimesters` (`trimester`,`no`) values (%s,%s);'
  for elem in zip(dates, varlist):
    mycursor.execute(sql, elem)
    mydb.commit()
  

  