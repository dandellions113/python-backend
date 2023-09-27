import loader
import Scraper
keyword="Finance Ministry"
toi_scraper=Scraper.TimesOfIndia(keyword)
toi_scraper.search_keyword()
toi_scraper.each_article_content()
loader.main(toi_scraper.file_path,keyword)