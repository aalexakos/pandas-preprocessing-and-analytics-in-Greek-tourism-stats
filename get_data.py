import pandas as pd
from collections import Counter
import os

def get_total_arrivals():
    total_arrivals=0
    arrivals=[]
    no=-2
    #searching in the 4th excel file of every year and getting the last line which indicates total number of passengers
    for year in range (2011,2015):
        df = pd.read_excel("./excel/"+str(year)+"/"+str(4)+"/1.xls",'DEC')
        df.columns = ['index','countries','air','railway','sea','road','total']
        #this while loop is used because the last line of the excel doesnt really indicates total number of passengers beacause last lines contain some text
        while no > -5:
            try:
                total_arrivals += int(df["total"].iloc[no])
                arrivals.append(int(df["total"].iloc[no]))
                break
            except:
                no-=1
    arrivals.append(total_arrivals)
    return arrivals

def get_most_visits_per_country():
    countries=[]
    cntr={}
    for year in range (2011,2015):
        i=-2
        df = pd.read_excel("./excel/"+str(year)+"/"+str(4)+"/1.xls",'DEC')
        df.columns = ['index','countries','air','railway','sea','road','total']
        df = df[df.countries != 'TOTAL ARRIVALS']
        df = df[df.countries != 'of which:']
        while i>-62 :
            if(not pd.isnull(df['countries'].iloc[i])):              
                cntr[df.iloc[i,1]] = int(df["total"].iloc[i])     
                
            i-=1
        #adding to list of dictionaries named countries, the temp dictionary cntr which contains every year's total tourists per country    
        countries.append(cntr.copy())

        #export to csv
        outname = str(year)+'.csv'
        outdir = './csv'
        if not os.path.exists(outdir):
            os.mkdir(outdir)

        fullname = os.path.join(outdir, outname)
        df.to_csv(fullname)

    #suming every year from countries list of dictionaries
    total_countries = {}
    for d in countries:
        for k in d.keys():
            total_countries[k] = total_countries.get(k,0) + d[k]

    sort_total = sorted(total_countries.items(), key=lambda x: x[1], reverse=True)
   
    return sort_total

get_most_visits_per_country()
def arrivals_by_means_of_transport():
    #dictionary means will contain every mean of transport as key and their total tourists as value
    means={}
    no=-2
    #searching in the 4th excel file of every year and getting the last line which indicates total number of passengers
    for year in range (2011,2015):
        df = pd.read_excel("./excel/"+str(year)+"/"+str(4)+"/1.xls",'DEC')
        df.columns = ['index','countries','air','railway','sea','road','total']

        #this while loop is used because the last line of the excel doesnt really indicates total number of passengers beacause last lines contain some text
        while no > -5:
            try:
                x=means.setdefault ("air" , int(df['air'].iloc[no]))
                x=means.setdefault ("railway",  int(df['railway'].iloc[no]))
                x=means.setdefault ("sea", int(df['sea'].iloc[no]))
                x=means.setdefault ("road", int(df['road'].iloc[no]))
                break
            except:
                no-=1
    
    return means

def get_tourists_per_trimester():
    total=[]
    tempList=[]
    no=-2
    temp=0
    #searching in the 4th excel file of every year and getting the last line which indicates total number of passengers
    for year in range (2011,2015):
        
        xls = pd.ExcelFile("./excel/"+str(year)+"/"+str(4)+"/1.xls")
        #parse excel sheet every three months 
        for i in range (2,12,3):
            df=xls.parse(i)
            df.columns = ['index','countries','air','railway','sea','road','total']
            #this while loop is used because the last line of the excel doesnt really indicates total number of passengers beacause last lines contain some text
            while no > -5:
                try:
                    #initializing my tempory variable and list every first semester of the year
                    if((year==2012 or year==2013 or year == 2014) and i==2):
                        temp=0
                        tempList.clear()  
                    temp=sum(tempList)
                    
                    #insert in the end of our list, trimester's total tourists
                    tempList.insert(len(tempList),int(df["total"].iloc[no])-temp)  
                    break           
                except:
                    no-=1
        #copying the temporary list that contains every year's tourists per trimester, to a list that contains all years
        total.append(tempList.copy())
    #total is a list of lists so flat_total is total list flattened 
    flat_total = [item for sublist in total for item in sublist]
    return (flat_total)
get_tourists_per_trimester()