from pyrebase import pyrebase

firebaseConfig = {
    "apiKey": "AIzaSyCxujiFsfdNZEH8zIxIQwaAXvujQvSFyA4",
    "authDomain": "smart-energy-3e7aa.firebaseapp.com",
    "databaseURL": "https://smart-energy-3e7aa-default-rtdb.firebaseio.com",
    "projectId": "smart-energy-3e7aa",
    "storageBucket": "smart-energy-3e7aa.appspot.com",
    "messagingSenderId": "8984393302",
    "appId": "1:8984393302:web:e1d193912f96b7d68d6df7",
    "measurementId": "G-RKB971HGGY"
}


class FirebaseDB:

    def __init__(self) -> None:
        super().__init__()
        self.db = pyrebase.initialize_app(firebaseConfig).database()

    def clear(self):
        self.db.remove()

    def insert(self, header, collection, data):
        self.db.child(header).child(collection).push(data=data)
