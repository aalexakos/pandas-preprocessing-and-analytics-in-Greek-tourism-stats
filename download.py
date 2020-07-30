import requests
import os
from bs4 import BeautifulSoup
import pandas as pd


def download_html():
    #download html files
    for year in range(2011 ,2015):
            if not os.path.exists("./html/" + str(year) + "/"):
                os.makedirs(os.path.dirname( "./html/" + str(year) + "/"))
            for trimester in range(1 , 5):
                #Create URLs to download the html pages
                url =  str(year) + "-Q" + str(trimester) 
                print("Downloading HTML: " + url)
                
                #Download the html pages
                html = 'https://www.statistics.gr/en/statistics/-/publication/STO04/' + url
                r = requests.get(html, allow_redirects=True)

                #save it in its coresponding folder
                open('./html/' + str(year)  + '/' + str(trimester) + '.html', 'wb').write(r.content)

def download_excel():
    #Get Excel files
    for year in range(2011 ,2015):
        for trimester in range(1 , 5):
            if not os.path.exists("./excel/" + str(year) + "/" + str(trimester) + "/" ):
                #make folders if they do not exist
                os.makedirs(os.path.dirname( "./excel/" + str(year) + "/" + str(trimester) + "/" ))
            
            #Parse html and get URLs for excel files
            soup = BeautifulSoup(open("./html/" + str(year) + "/" + str(trimester) + ".html", encoding='utf8'), 'html.parser')
            href = soup.findAll("table", {"class": "documentsTable"})[2].find_all("a")[2]["href"]
            print("Downloading excel file for year :" + str(year) + " and trimester: " + str(trimester))

            #Download the excel files
            excel = href
            r = requests.get(excel, allow_redirects=True)
                
            #save them in their coresponding folder
            open('./excel/' + str(year)  + '/' + str(trimester) + "/" +  '1.xls', 'wb').write(r.content)
download_html()
download_excel()
for year in range(2011 ,2013):
    for trimester in range(1 , 5):
        df = pd.read_excel("./excel/"+str(year)+"/"+str(trimester)+"/1.xls")
        df.columns = ['index','countries','air','railway','sea','road','total']
        df.drop(df.index[[0,1]])
        


for year in range(2013 ,2015):
    for trimester in range(1 , 5):
        df = pd.read_excel("./excel/"+str(year)+"/"+str(trimester)+"/1.xls")
        df.columns = ['index','countries','air','railway','sea','road','total']
        df.drop(1)
