import tweetnlp
# import db_download
import db_upload
import json
import time
def main(path,keyword):
    with open(path,"r",encoding='utf-8') as f:
        data=json.loads(f.read())
    model1 = tweetnlp.load_model('sentiment')  # Or `model = tweetnlp.Sentiment()` 

    towrite=[]
    for i in data:
        # print(type(i))
        temp=i['Headline']
        tsen=model1.sentiment(temp)
        i['sentiment']=tsen["label"]
        i['cms']=i['Img'].endswith(".cms")
        i['time']=time.time()
        towrite.append(i)
    db_upload.main(towrite)


if __name__ == "__main__":
    main("data/times_of_india/","Finance Ministry")




# with open("out_json/processed_Defence Ministry_data.json", 'w', encoding='utf-8') as json_file:
#     json.dump(towrite,json_file,indent=4)



# # print(model.sentiment("opposition is so bad that the ruling party's word is final"))# Or `model.predict`
# sen=model1.sentiment("opposition is so bad that the ruling party's word is final", return_probability=True)
# iro=model2.irony("opposition is so bad that the ruling party's word is final", return_probability=True)
# print("sentiment:",sen["label"],sen["probability"][sen["label"]])
# print("irony:",iro["label"],iro["probability"][iro["label"]])
