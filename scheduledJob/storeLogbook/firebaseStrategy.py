from .firebaseController import FirebaseController

def uploadToFirebase(df):
    print("uploading entries to firebase")

    logbookRef = FirebaseController.setup().logbookRef
    #empty the ref first
    logbookRef.set({})
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
    
   

    