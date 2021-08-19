# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 01:14:32 2021

@author: Kevin Sebineza
"""

from bs4 import BeautifulSoup
import requests

import sys

# List variables 
logo_arr = []
address_arr = []
web_arr = []
phone_arr = []
email_arr = []
pHeads_arr = []
kClients_arr = []
membership_arr = []
lawyers_arr = []

# Function to get the details from the specified law firms
def get_details(link):
        
    source = requests.get(link).text
    soup = BeautifulSoup(source, 'lxml')
    
    try:
        # Getting the logo
        logo = soup.find('img', class_='firm-profile-logo legal500-item')
        logo_url = "https://www.legal500.com"+logo.get('data-lazy-src')
        logo_arr.append(logo_url)
    except:
        pass

    try:
        # Getting the address
        add = soup.find('div', class_='address-box')
        a = add.address.text.split('\n')[2].strip().replace('   ', '')
        address_arr.append(a)
    except:
        pass
    
    try:
        # Getting the company website
        web = soup.find('a', class_='firm-website')
        web_arr.append(web.get('href'))
    except:
        pass
    
    try:
        # Getting phone number
        phone = soup.find('div', class_='contact-links')
        phone_arr.append(phone.text.split('\n')[1].strip()[27:-18])
    except:
        pass
    
    try:
        # Getting the email address
        email = soup.find('a', class_='firm-email')
        email_arr.append(email.get('href')[7:-33])
    except:
        pass
    
    try:
        # Getting the practice heads
        pHeads = soup.find('div', class_='practice-heads-list')
        pHeads_arr.append(pHeads.p.text)
    except:
        pass
    
    try:
        # Getting the key clients
        kClients = soup.find('div', class_='client-list')
        c = ""
        clients = kClients.find_all('p')
        for i in clients:
            c = c + i.text + ", "
        kClients_arr.append(c)
    except:
        pass
    
    try:
        # Getting the membership
        membership = soup.find('div', id='memberships_section')
        # listToString(membership.text.strip().split(',')[1:])
        member_list = membership.text.replace('\t', '').replace('\n', '')[11:].split(' ')
        members = ''
        for i in range(len(member_list)):
            if member_list[i] != '':
                members = members + member_list[i] + ", "
        membership_arr.append(members.replace('\n', ''))
    except:
        pass
    
    try:
        # Getting list of lawyers
        lawyer_names = ''
        for lawyers in soup.find_all('table', id='lawyer-profiles-list'):
            for name in lawyers.find_all('td', class_='profile-name'):
                lawyer_names = lawyer_names + name.text + ", "
                lawyers_arr.append(lawyer_names)
    except:
        pass

# Main
if __name__ == '__main__':  
    user_link = sys.argv[1]
    get_details(user_link)
    print("Logo: ", logo_arr, "\n",
          "Address: ", address_arr, "\n",
          "Website: ", web_arr, "\n",
          "Phone Number: ", phone_arr, "\n",
          "Email: ", email_arr, "\n",
          "Practice Heads: ", pHeads_arr, "\n",
          "Key Clients: ", kClients_arr, "\n",
          "Membership : ", membership_arr, "\n",
          "Lawyers: ", lawyers_arr, "\n")