from bs4 import BeautifulSoup
import requests
import json


class TimesOfIndia:
    def __init__(self, keyword):
        self.base_url = "https://timesofindia.indiatimes.com/"
        self.keyword = keyword
        self.file_path = f'data/times_of_india/{self.keyword}_data.json'

    def search_keyword(self):

        search_url = f"{self.base_url}topic/{self.keyword}"

        response = requests.get(search_url)

        if response.status_code == 200:
            html_content = response.text

            soup = BeautifulSoup(html_content, 'html.parser')

            target_divs = soup.find_all('div', class_='uwU81')
            extracted_data = []

            for div in target_divs:
                headline = div.find('span').text.strip()
                timestamp = div.find('div', class_='ZxBIG').text.strip()
                description = div.find('p', class_='oxXSK').text.strip()

                link = div.find('a')['href']
                img = div.find('img')['src']

                data = {
                    "Headline": headline,
                    "Timestamp": timestamp,
                    "Description": description,
                    "Link": link,
                    "Img": img
                }

                extracted_data.append(data)

            with open(self.file_path, 'w', encoding='utf-8') as json_file:
                json.dump(extracted_data, json_file,
                          ensure_ascii=False, indent=4)

        else:
            print(
                f'Failed to retrieve the webpage for keyword "{keyword}". Status code:', response.status_code)

    def get_article_content(self, article_url):
        response = requests.get(article_url)
        if response.status_code == 200:
            html_content = response.text

            soup = BeautifulSoup(html_content, 'html.parser')

            script_tags = soup.find_all('script', type='application/ld+json')

            content = ""

            for script_tag in script_tags:
                try:
                    data = json.loads(script_tag.string)
                    if "@type" in data and data["@type"] == "NewsArticle":
                        content = data.get("articleBody", "")
                        break
                except json.JSONDecodeError:
                    continue

            return content

    def each_article_content(self):
        with open(self.file_path, 'r', encoding='utf-8') as json_file:
            article_data = json.load(json_file)
            for article in article_data:
                article['content'] = self.get_article_content(article['Link'])

        with open(self.file_path, 'w', encoding='utf-8') as json_file:
            json.dump(article_data, json_file, ensure_ascii=False, indent=4)


class TheHindu:
    def __init__(self, keyword):
        self.base_url = "https://www.thehindu.com/"
        self.keyword = keyword
        self.file_path = f'data/the_hindu/{self.keyword}_data.json'


# Example usage:
if __name__ == "__main__":
    keyword = "Finance Ministry"  # Replace with your desired keyword
    toi_scraper = TimesOfIndia(keyword)
    toi_scraper.search_keyword()
    toi_scraper.each_article_content()
