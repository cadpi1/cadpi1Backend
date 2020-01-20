import sqlite3
import os
from sqlite3 import Error
from getUKCCredentials import getUKCCredentials

#Make a directory for storing data
os.mkdir("./data")
print("Made directory for data storage")

#Create the sqlite db for the blog
con= sqlite3.connect("data/blog.db")
c = con.cursor()
print("Created blog database")

#Create the table for the logbook
c.execute('''CREATE TABLE "logbook" (
    "Session Type" TEXT,
"Climb name" TEXT,
  "Grade" TEXT,
  "Style" TEXT,
  "Partner(s)" TEXT,
  "Notes" TEXT,
  "Date" TEXT,
  "Crag name" TEXT
)''')

print("Created database table for logbook")

#Create .env file
if not os.path.exists('./.env'):
    open("./.env", "x")

#Make user get ukc credentials
getUKCCredentials()

print("Stored credentials for scraping")