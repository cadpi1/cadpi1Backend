import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import os

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

class FirebaseController:
    initialised = False
    logbookref = None

    def setup():
        if not FirebaseController.initialised:
             # Fetch the service account key JSON file contents
            cred = credentials.Certificate(os.path.join(THIS_FOLDER, 'key.json'))
            # Initialize the app with a service account, granting admin privileges
            firebase_admin.initialize_app(cred, {
                'databaseURL': 'https://blog-b50fa.firebaseio.com/'
            }) 
            FirebaseController.logbookRef = db.reference('/logbook')

            initialised = True

            return FirebaseController
        return FirebaseController

    
       
