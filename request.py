from gnews import GNews
import json
def main(lang,keyword,fname):
	google_news = GNews(language=lang, country='IN', period='7d', start_date=None, end_date=None, max_results=10)
	news = google_news.get_news(keyword)
	for i in news:
		i['lang']=lang
	# with open(f"in_json/{fname}_{lang}.json", 'w', encoding='utf-8') as json_file:
	# 	json.dump(news,json_file,indent=4,ensure_ascii=False)
	return news
if __name__=="__main__":
	json.dump(main("hi","वित्त","main"),open("news.json","w",encoding='utf-8'),indent=4,ensure_ascii=False)