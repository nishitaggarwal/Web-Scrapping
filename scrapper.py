from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
import pandas as pd

START_URL = 'https://en.m.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'

browser = webdriver.Chrome('C:/Users/HP/Documents/projects/class_127_2/chromedriver.exe')
browser.get(START_URL)
time.sleep(10)
def scrape():
    
    
    soup = BeautifulSoup(browser.page_source,"html.parser")
    
    star_table  = soup.find("table")
        
    tr_rows = star_table.find_all("tr")
    
    
    temp_list = []
    for tr in tr_rows:
        td = tr.find_all("td") 
        td_row = [i.text.rstrip() for i in td]
        temp_list.append(td_row)
    
    star_name = []
    distance = []
    mass = []
    radius = []
    luminosity = []
    for i in range(1,len(temp_list)):
        star_name.append(temp_list[i][1])
        distance.append(temp_list[i][3])
        mass.append(temp_list[i][5])
        radius.append(temp_list[i][6])
        luminosity.append(temp_list[i][7])
        
       
    df2 = pd.DataFrame(list(zip(star_name,distance,mass,radius,luminosity)), columns = 
                       ["Star Name","Distance","Mass","Radius","Luminosity"])
    df2.to_csv('Bright_stars.csv')
        
scrape()
