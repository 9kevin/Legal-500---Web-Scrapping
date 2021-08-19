# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 17:36:38 2021

@author: ALU Student 100
"""

import pandas as pd

from bs4 import BeautifulSoup
import requests

import sys

# Array variables
name_arr = []
location_arr = []
link_arr = []



def get_info(link):
    
    source = requests.get(link).text
    soup = BeautifulSoup(source, 'lxml')
    
    # Getting information from single-offices
    for firm in soup.find_all('li', class_='single-office'):
        name = firm.a.strong.text
        name_arr.append(name)
        location = firm.a.text.split('\n')[-1].strip()
        location_arr.append(location)
        link = 'https://www.legal500.com'+firm.a['href']
        link_arr.append(link)
        
    # Getting information from multiple offices
    for info in soup.find_all('li', class_='multiple-offices'): 
        name = info.text.split('\n')[1].strip()
        for link in info.find_all('a'):
            if info.text.split('\n')[1].strip() == name:
                name_arr.append(name)
                location_arr.append(link.text)
                link_arr.append('https://www.legal500.com'+link['href'])
    
    # Creating a dataset
    df = pd.DataFrame({'Company Name':name_arr, 'Location': location_arr, 'Link': link_arr})
    return df

# Function turning a list into a string
def listToString(s): 
    str1 = " "   
    return (str1.join(s))


if __name__ == '__main__':  
    user_link = sys.argv[1]
    df = get_info(user_link)
    print(df)
    df.to_csv('legal_firms_data.csv')