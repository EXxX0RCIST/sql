import requests # используется там где скорость только мешает 
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse, urlunparse
from googlesearch import search # простейший поиск в google
from collections import OrderedDict # для работы со списками
import time

class DorkParser:

    def __init__(self) -> None:
        self.urls = []
        self.get_params = set()
        self.TIME_SLEEP = 300 # pause search google 
        self.RESULT_SEARCH = 50 # search google dork (max 99)

    def set_time_sleep(self, time_slep):
        self.TIME_SLEEP = time_slep
        print(f"Time sleep={time_slep}")

    def set_result_search(self, result):
        self.RESULT_SEARCH = result
        print(f"Result search google dork={result}")

    def pars_dork(self, dork):
        try:
            for result in search(dork, num_results=self.RESULT_SEARCH):
                self.urls.append(result)
        except Exception as e:
            print(f'An error occurred while searching for google dork\n"{dork}": {e}')

    # в этой функции все работает только благодаря неведомым силам, лучше туда не лезть
    def check_links_for_page(self):
        try:
            for url in self.urls:
                target = self.trim_url(url) # обрезка ссылки
                print(f"Parsing {target}")
                try:
                    response = requests.get(target, timeout=5)
                    response.raise_for_status()  # Проверка на ошибки HTTP
                except requests.RequestException as e:
                    return False

                soup = BeautifulSoup(response.text, 'html.parser')
                
                links = [] # все сслылки
                for link in soup.find_all('a', href=True):
                    full_link = urljoin(target, link['href'])
                    links.append(full_link)
                
                # valid_links = [] #  только рабочие ссылки
                # valid_links.append(target)
                for page in links:
                    if "http" not in page:
                        continue
                    if '=' not in page:
                        continue
                    try:
                        # parsed_url = urlparse(page)
                        
                        # # Удаление GET параметров, заменяя их на пустую строку
                        # trimmed_url = urlunparse((parsed_url.scheme, parsed_url.netloc, parsed_url.path, parsed_url.params, '', parsed_url.fragment))

                        response = requests.get(page, timeout=5)
                        response.raise_for_status() # Проверка на валидност
                        self.get_params.add(page)
                    except requests.RequestException as e:
                        continue

                # valid_links = list(OrderedDict.fromkeys(valid_links)) # удаление дублей
                
        except Exception as e:
            print(e)


    def trim_url(self, url):
        parsed_url = urlparse(url)
        base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
        return base_url

    def main_pars(self):
        print("Start performing a search")
        with open('dorks.txt', 'r', encoding='utf-8') as dorks:
            for d in dorks:
                d = d.rstrip('\n')
                print(f"Search by dork {d}")
                start_time = time.time()
                self.pars_dork(d)
                self.check_links_for_page()
                self.urls = []
                finish_time = time.time()
                work_time = finish_time - start_time
                if self.TIME_SLEEP > work_time:
                    time.sleep(self.TIME_SLEEP - work_time)                
            with open('targets.txt', 'a') as targets:
                for target in self.get_params:
                    targets.write(f'{target}\n')

# сборщик мусора python я очень надеюсь на тебя 