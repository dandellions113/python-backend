import tweetnlp
# import db_download
# import db_upload
import json
import time
model1 = tweetnlp.load_model('sentiment', multilingual=True)
def main(lst,keyword):
    # with open(path,"r",encoding='utf-8') as f:
    #     data=json.loads(f.read())
      # Or `model = tweetnlp.Sentiment()` 
    # print(lst)
    towrite=[]
    for i in lst:
        # print(type(i))
        temp=i['title']
        tsen=model1.sentiment(temp)
        i['sentiment']=tsen["label"]
        # i['cms']=i['Img'].endswith(".cms")
        i['time']=time.time()
        i['keyword']=keyword
        towrite.append(i)
    return towrite


if __name__ == "__main__":

    x=main(json.load(open("news.json","r",encoding='utf-8')),"वित्त")
    #dump x to json
    with open("temp.json","w",encoding='utf-8') as f:
        json.dump(x,f,indent=4,ensure_ascii=False)



# with open("out_json/processed_Defence Ministry_data.json", 'w', encoding='utf-8') as json_file:
#     json.dump(towrite,json_file,indent=4)



# # print(model.sentiment("opposition is so bad that the ruling party's word is final"))# Or `model.predict`
# sen=model1.sentiment("opposition is so bad that the ruling party's word is final", return_probability=True)
# iro=model2.irony("opposition is so bad that the ruling party's word is final", return_probability=True)
# print("sentiment:",sen["label"],sen["probability"][sen["label"]])
# print("irony:",iro["label"],iro["probability"][iro["label"]])
