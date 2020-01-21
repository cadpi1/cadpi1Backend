import sqlite3
from flask import jsonify

#Returns the logbook data grouped by date
def getLogbookGroupedByDate():
    conn = sqlite3.connect(database="./data/blog.db")
    c = conn.cursor()
    c.execute('SELECT DISTINCT DATE from LOGBOOK')
    datesClimbed = c.fetchall()
    response = []
    climbs=[]
    for date in datesClimbed:
        c.execute('SELECT "Session Type", "Climb name", Grade, Style, "Partner(s)", Notes, "Crag name" from LOGBOOK where Date = ?', date)
        climbs = c.fetchall()
        climbList = []
        for climb in climbs:
            climbList.append(
                {"Session Type":climb[0],
                "Climb name":climb[1],
                "Grade":climb[2],
                "Style":climb[3], 
                "Partner(s)":climb[4] or "",
                "Notes":climb[5] or "",
                "Crag name":climb[6]}
            )
        response.append({
            'Date':date, 
            'Session Type':climbs[0][0],
            'Location':climbs[0][6],
            'Climbs':climbList
        })
    return jsonify(response)