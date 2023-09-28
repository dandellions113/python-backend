import firebase_admin
from firebase_admin import credentials
import json
from firebase_admin import firestore
cred = credentials.Certificate("news-room-c5326-firebase-adminsdk-74knj-cf6d064510.json")
firebase_admin.initialize_app(cred)
#connect to firebase firestore
def main(lst,keyword):
    db = firestore.client()
    #list all collections
    # collst=[i.id for i in db.collection(u'finance').list_documents()]
    curr=db.collection(f'{keyword}')
    for i in lst:
        curr.document(i['title']).set(i,merge=True)
    
    
    
if __name__ == "__main__":
    main(json.load(open("in_json/defence_pa.json","r",encoding='utf-8')),"temp")