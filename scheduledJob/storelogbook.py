import pandas 
import os
import sqlite3
import sqlalchemy
from utils import ukcScraperUtils as utils
import datetime

#Read the spreadsheet previously downloaded
df = pandas.read_excel("./spreadsheet.xls") 

#Get the date of the last thing stored in the logbook
#If it is the first time doing it, instead create date 1970 (to include all entries)
conn = sqlite3.connect(database="../data/blog.db")
c = conn.cursor()
c.execute('SELECT Date from LOGBOOK order by Date desc limit 1')
result = c.fetchone()
maxDate=None
if(result!=None):
    maxDate = datetime.datetime.strptime(result[0], '%Y-%m-%d').date()
    print("Last log in database was on :")
    print(maxDate)
else:
    maxDate=datetime.datetime.strptime("70/Jan/01", "%y/%b/%d").date()
    print("No previous log found in database")

#Make the date string a pandas date, to keep data ordered
df['Date'] = pandas.to_datetime(df['Date'], format="%d/%b/%y").dt.date

#Add the session type to the df (not included in UKC logbook)
df['Session Type'] = df.apply(lambda x: utils.determineSessionTypeFromUKCGradeString(x['Grade']), axis=1)

#Filter the pandas df to only keep entries done after the last logged date
df = df[df['Date'] > maxDate]
print(""+str(len(df))+" entries will be added")

#Store the logbook entries into the logbook table
#Need to use sqlalchemy because of a bug in pandas with sqlite3
engine = sqlalchemy.create_engine('sqlite:///home/cadpi/cadpi1Backend/data/blog.db')
df.to_sql('logbook', con=engine, if_exists="append", index=False)

#Delete the now unused spreadsheet to save space
os.remove('./spreadsheet.xls')

