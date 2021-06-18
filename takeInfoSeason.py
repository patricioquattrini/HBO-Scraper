import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from search_id_in_page_source import search_id
from season import Season
from getInfoMovies import getInfoMovies
import requests
import json

def takeInfoSeason(driver, list_of_ids, list_of_serie_and_info):

    for id in list_of_ids:
        magic_url = "https://api-cache-b.hbogola.com/contentgw/v7.0/Content/SPA/COMP/" + id + "/f5d80122-51d5-46c6-bcf0-ec3b73b2e45b"
        response = requests.get(magic_url)
        res_json = json.loads(response.text)

        for season_id in res_json["ChildContents"]["Items"]:
            magic_url = "https://api-cache-b.hbogola.com/contentgw/v7.0/Content/SPA/COMP/" + season_id["Id"] + "/f5d80122-51d5-46c6-bcf0-ec3b73b2e45b"
            response = requests.get(magic_url)
            res_json = json.loads(response.text)
            season = Season(res_json["Id"],
                            res_json["Name"],
                            season_id["Name"],
                            res_json["ProductionYear"] if res_json.get("ProductionYear") else None,
                            res_json["AgeRatingName"] if res_json.get("AgeRatingName") else None,
                            res_json["Abstract"] if res_json.get("Abstract") else None,
                            getEpisodes(driver, season_id))
        list_of_serie_and_info.append(season)

def getEpisodes(driver, season_id):
    driver.get("https://www.hbogola.com/content/" + season_id["Id"])
    time.sleep(2)
    episodes = driver.find_elements_by_xpath('//img[@class="thumbImage loaded"]')
    episodes_x_season = []
    for episode in episodes:

        hover = ActionChains(driver).move_to_element(episode)
        hover.perform()
        page_source = driver.find_elements_by_xpath('//div[@class="expandedContentWrapper"]')
        page_source = driver.page_source
        id = search_id(page_source)
        time.sleep(0.7)
        getInfoMovies(id, episodes_x_season)
    return episodes_x_season