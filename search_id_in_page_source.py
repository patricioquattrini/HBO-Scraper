from bs4 import BeautifulSoup
import time

def search_id(page_source):
    soup = BeautifulSoup(page_source, "html.parser")
    time.sleep(0.1)
    id_content = soup.find_all("div", class_="expandedContentWrapper")
    id_a = id_content[0].find_all("a")
    id = id_a[0]["href"]
    return id.replace("/content/","")