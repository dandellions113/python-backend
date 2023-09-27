import firebase_admin
from firebase_admin import credentials
import json
from firebase_admin import firestore
cred = credentials.Certificate("news-room-c5326-firebase-adminsdk-74knj-cf6d064510.json")
firebase_admin.initialize_app(cred)
#connect to firebase firestore
def main(lst):
    db = firestore.client()
    #add data to firestore
    # lst=json.loads(open("out_json/test.json","r").read())
    #add this list of news as a list of documents to firestore
    for i in lst:
        db.collection("news").set(i)
if __name__ == "__main__":
    main([])