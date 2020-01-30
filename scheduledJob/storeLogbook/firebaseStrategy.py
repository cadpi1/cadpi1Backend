from .firebaseController import FirebaseController

def reversedDate(date):
    parts = date.split("/")
    return parts[2]+"/"+parts[1]+"/"+parts[0]

def uploadToFirebase(df):
    print("uploading entries to firebase")

    logbookRef = FirebaseController.setup().logbookRef
    #empty the ref first
    logbookRef.set({})
    #Make the date field into format Y-M-D (by default d-m-y)
    df['Date'] = df['Date'].map(lambda x:reversedDate(x))

    groupedByDate = df.groupby(['Date'])

    for date, values in groupedByDate:
        climbList = []
        for index, row in values.iterrows():
            climbList.append(
                {
                "Grade":row['Grade'],
                "Session Type":row['Session Type'],
                "Climb name":row['Climb name'],
                "Style":row["Style"],
                "Partner(s)":row['Partner(s)'],
                "Notes":row['Notes'],
                "Crag name":row['Crag name']
                }
            )
        logbookRef.push({
            'Date':date, 
            'Session Type':climbList[0]["Session Type"],
            'Location':climbList[0]["Crag name"],
            'Climbs':climbList
        })
    
   

    