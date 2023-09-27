import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json
cred = credentials.Certificate("news-room-c5326-firebase-adminsdk-74knj-cf6d064510.json")
firebase_admin.initialize_app(cred)
#get all documents from collection for firestore
def main():
    db = firestore.client()
    docs=db.collection("news").stream()
    lst=[]
    for doc in docs:
        lst.append(doc.to_dict())
    return lst
if __name__ == "__main__":
    with open("test.json","w") as f:
        json.dump(main(),f,indent=4)