import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time


Start_Url = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
browser = webdriver.Chrome('C:/Users/HP/Documents/projects/class_127_2/chromedriver.exe')
browser.get(Start_Url)

time.sleep(5)
def scrape():
    page = requests.get(Start_Url)

    soup = BeautifulSoup(page.text,'html.parser')

    star_table = soup.find_all('table')
   # print(star_table[5])
    table_rows = star_table[5].find_all('tr')
    temp_list = []


    for tr in table_rows:
        td = tr.find_all("td") 
        td_row = [i.text.rstrip() for i in td]
        temp_list.append(td_row)
        
    star_name = []
    distance = []
    mass = []
    radius = []
    print(len(temp_list))
    for i in range(1,len(temp_list)):
            star_name.append(temp_list[i][0])
            distance.append(temp_list[i][5])
            mass.append(temp_list[i][7])
            radius.append(temp_list[i][8])
        
        

    df2 = pd.DataFrame(list(zip(star_name,distance,mass,radius)), columns = 
                        ["Star Name","Distance","Mass","Radius"])
    df2.to_csv('Dwarf_Planets_data.csv')


scrape()