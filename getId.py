import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from search_id_in_page_source import search_id
from getInfoMovies import getInfoMovies
from takeInfoSeason import takeInfoSeason
from convert_dict_json import convert_dict_json
import requests
import json
import os
import string

list_of_serie_and_info = []

list_of_season_ids = []
list_of_movie_and_info = []

list_of_json_movies = {}
list_of_json_movies["movies"] = []
list_of_json_movies["series"] = []

def getIds(driver, url, is_a_movie):
    driver.get(url)
    time.sleep(4)
    viewAllContent(driver)
    elems = driver.find_elements_by_xpath('//img[@class="thumbImage loaded"]')
    if is_a_movie:
        for elem in elems:
            hover = ActionChains(driver).move_to_element(elem)
            hover.perform()
            page_source = driver.find_elements_by_xpath('//div[@class="expandedContentWrapper"]')
            page_source = driver.page_source
            id = search_id(page_source)
            getInfoMovies(id, list_of_movie_and_info)
            convert_dict_json(list_of_movie_and_info, list_of_json_movies, "movies")
    else:
        for elem in elems:
            list_of_season_ids.append(extracId(driver, elem))
        takeInfoSeason(driver, list_of_season_ids, list_of_serie_and_info)
        convert_dict_json(list_of_serie_and_info, list_of_json_movies, "series")

def viewAllContent(driver):
    for c in string.ascii_uppercase:
        try:
            elem = driver.find_element_by_name(c)
            elem.send_keys(Keys.ENTER)
            time.sleep(1)
        except:
            pass

def extracId(driver, elem):
    hover = ActionChains(driver).move_to_element(elem)
    hover.perform()
    page_source = driver.find_elements_by_xpath('//div[@class="expandedContentWrapper"]')
    page_source = driver.page_source
    id = search_id(page_source)
    time.sleep(0.4) # esto lo agrego ya que no estoy usando una func getAlgo para obtener la info
    return id
