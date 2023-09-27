import firebase_admin
from firebase_admin import credentials
import json
from firebase_admin import firestore
cred = credentials.Certificate("news-room-c5326-firebase-adminsdk-74knj-cf6d064510.json")
firebase_admin.initialize_app(cred)
#connect to firebase firestore
def main(lst):
    db = firestore.client()
    #list all collections
    collst=[i.id for i in db.collection(u'news').list_documents()]
    curr=db.collection(u'news')
    for i in lst:
        curr.document(i['Headline']).set(i,merge=True)
    
    
    
if __name__ == "__main__":
    main([{
        "Headline": "Oil prices a concern but not alarming yet: finance ministry",
        "Timestamp": "TNN / Sep 23, 2023, 04:46 (IST)",
        "Description": "The Indian government, in its August economic report, expressed comfort with a projected 6.5% growth for 2023-24. It acknowledged concerns about rising global crude oil prices and the August monsoon deficit but highlighted positive factors like corporate profitability, private sector investments, and construction activity. While it recognized risks like a stock market correction and geopolitical developments, it believed that the impact on India's economic activity would likely be limited.",
        "Link": "https://timesofindia.indiatimes.com/business/india-business/oil-prices-a-concern-but-not-alarming-yet-finance-ministry/articleshow/103877620.cms",
        "Img": "https://static.toiimg.com/thumb/imgsize-123456,msid-103877620,width-300,resizemode-4/103877620.jpg",
        "content": "NEW DELHI: The government is comfortable with its estimate of 6.5% growth for 2023-24 but the recent surge in global crude oil prices is a concern although not alarming yet, the finance ministry's monthly economic report for August said on Thursday.\"As always, risks remain. Crude oil prices are steadily climbing. The monsoon deficit in August could impact both Kharif and Rabi crops. That needs to be assessed. However, it is heartening that rains in September have erased a portion of the rainfall deficit at the end of August,\" said the report.\"A stock market correction, in the wake of an overdue global stock market correction, is an ever-present risk. Offsetting these risks are the bright spots of corporate profitability, private sector capital formation, bank credit growth and activity in the construction sector,\" it said.The report said that India's economic outlook for FY24 remains bright and economic activity maintained its momentum. It further said that high frequency indicators suggest that the second quarter of FY24 is shaping up well too. The monsoon deficit of August has been partially plugged in September and that is good news. \"Prices of selected food items that drove the inflation rate above 7% in July are on the retreat. Private sector is in good health as data on advance tax payments for the second quarter confirm. They are investing,\" the report said.The report said the risks of a stock market correction and geopolitical developments could potentially hurt investment sentiment in the second half of the financial year. \"But, the impact of these developments on underlying economic activity in India should be relatively contained,\" said the report prepared by the department of economic affairs.It said the structural reforms undertaken for promoting ease of doing business, logistical efficiency, and infrastructure creation are accelerating job creation and formalisation of the economy. \"The issues that unorganised workers face resulted in the creation of a comprehensive database of e-Shram Portal (with more than 29 crore registrations) and a host of customised social security schemes,\" the report added."
    }])