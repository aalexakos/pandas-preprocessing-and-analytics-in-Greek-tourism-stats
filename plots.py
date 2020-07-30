import matplotlib.pyplot as plt
import numpy as np
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Bilbo83os",
  database="elstat"
)
def plot_trimesters():

  #download data from database
  mycursor = mydb.cursor()
  mycursor.execute("select trimester from trimesters")
  column = mycursor.fetchall()
  mycursor.execute("select no from trimesters")
  row = mycursor.fetchall()

  #making list of lists flat to use them in plots
  flat_row = [item for sublist in row for item in sublist]
  flat_column = [item for sublist in column for item in sublist]

  #ploting as bars
  plt.figure(figsize=(12, 9))
  plt.yticks(np.arange(0, max(flat_row), 1000000))
  plt.xlabel("trimsters")
  plt.ylabel("tourists per trimester x10^7")
  plt.bar(flat_column,flat_row,align='center')

  plt.show()

def plot_countries():
  #download data from database
  mycursor = mydb.cursor()
  mycursor.execute("select country from countries")
  column = mycursor.fetchall()
  mycursor.execute("select no from countries")
  row = mycursor.fetchall()

  #making list of lists flat to use them in plots
  flat_row = [item for sublist in row for item in sublist]
  flat_column = [item for sublist in column for item in sublist]

  #ploting as bars
  plt.figure(figsize=(16, 9))
  plt.yticks(np.arange(0, max(flat_row), 1000000))
  plt.xticks(rotation='vertical')
  plt.xlabel("countries")
  plt.ylabel("tourists per country")
  plt.bar(flat_column,flat_row,align='center')

  plt.show()

def plot_means_of_transport():
  #download data from database
  mycursor = mydb.cursor()
  mycursor.execute("select means from means_of_transport")
  column = mycursor.fetchall()
  mycursor.execute("select no from means_of_transport")
  row = mycursor.fetchall()  

  #making list of lists flat to use them in plots
  flat_row = [item for sublist in row for item in sublist]
  flat_column = [item for sublist in column for item in sublist]
  
  #ploting as bars
  plt.figure(figsize=(5, 5))
  plt.yticks(np.arange(0, max(flat_row), 1000000))
 
  plt.xlabel("means of transport")
  plt.ylabel("numbers of means used")
  plt.bar(flat_column,flat_row,align='center')

  plt.show()


def plot_total_arrivals():
  #download data from database
  mycursor = mydb.cursor()
  mycursor.execute("select year from total_arrivals")
  column = mycursor.fetchall()
  mycursor.execute("select arrivals from total_arrivals")
  row = mycursor.fetchall()  

  #making list of lists flat to use them in plots
  flat_row = [item for sublist in row for item in sublist]
  flat_column = [item for sublist in column for item in sublist]
  
  #ploting as bars
  plt.figure(figsize=(5, 5))
  plt.yticks(np.arange(0, max(flat_row), 10000000))
  plt.xlabel("year")
  plt.ylabel("arrivals")
  plt.bar(flat_column,flat_row,align='center')

  plt.show()

plot_countries()
plot_means_of_transport()
plot_total_arrivals()
plot_trimesters()