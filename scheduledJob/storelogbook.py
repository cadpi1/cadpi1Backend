import pandas 
import os
import sqlite3
import sqlalchemy
from utils import ukcScraperUtils as utils
import datetime
from storeLogbook import firebaseStrategy, sqlliteStrategy
from dotenv import load_dotenv
load_dotenv()

#Prepare the data previously downloaded
df = pandas.read_excel("./spreadsheet.xls") 
#Add the session type to the df (not included in UKC logbook)
df['Session Type'] = df.apply(lambda x: utils.determineSessionTypeFromUKCGradeString(x['Grade']), axis=1)
df = df.fillna('')

strategy = os.getenv("strategy")

if strategy == "firebase":
    firebaseStrategy.uploadToFirebase(df)
elif strategy == "sqllite":
    sqlliteStrategy.loadIntoDB(df)
    
#Delete the now unused spreadsheet to save space
os.remove('./spreadsheet.xls')

