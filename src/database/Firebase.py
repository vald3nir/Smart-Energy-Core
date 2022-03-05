import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

_path_json_config = 'src\database\smart-energy-3e7aa-5b8f1f0b31fd.json'
_firebase_config = {
    "apiKey": "AIzaSyCxujiFsfdNZEH8zIxIQwaAXvujQvSFyA4",
    "authDomain": "smart-energy-3e7aa.firebaseapp.com",
    "databaseURL": "https://smart-energy-3e7aa-default-rtdb.firebaseio.com",
    "projectId": "smart-energy-3e7aa",
    "storageBucket": "smart-energy-3e7aa.appspot.com",
    "messagingSenderId": "8984393302",
    "appId": "1:8984393302:web:e1d193912f96b7d68d6df7",
    "measurementId": "G-RKB971HGGY"
}


class FirebaseClient:

    def __init__(self) -> None:
        super().__init__()
        cred = credentials.Certificate(_path_json_config)
        firebase_admin.initialize_app(cred, _firebase_config)
        self.firestore = firestore.client()

    def insert(self, collection, document, data):
        doc_ref = self.firestore.collection(collection).document(document)
        doc_ref.set(data)
