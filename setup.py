import sqlite3
import os
from sqlite3 import Error
from getUKCCredentials import getUKCCredentials
from crontab import CronTab
from datetime import datetime

#Make a directory for storing data
os.mkdir("/home/cadpi/cadpi1Backend/data")
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
    print("Created env file")

#Add flask environment variable to env file
f = open('./.env', 'a')
f.write('FLASK_APP=api.api')
print("Added flask app env variable")

#Make user get ukc credentials
getUKCCredentials()
print("Stored credentials for scraping")

#Create cron job of scraping ukc logbook everyday at current time 
cron = CronTab(user='cadpi')
job = cron.new(command='./home/cadpi/cadpi1Backend/scheduledJob/scrapelogbook.sh')
now = datetime.now()
job.hour.every(23)
cron.write()
print("Created cron job to scrape UKC logbook")