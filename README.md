"# Legal-500---Web-Scrapping" 

The following python scripts help in mining law firms information from Legal 500 (https://www.legal500.com/). 

# Instructions on how to run the scripts:

1. The web_scrapping.py file extracts basic information about law firms in a given country directory (Ex: https://www.legal500.com/c/france/directory/). The script takes the url of the country directory and returns a csv file containing information about each law firm. 

You can run the script by simply going to the directory where the script is saved and run 'python web_scrapping.py [url]'.

2. The firm_details.py file receives a link of the law firm (which can be found from the previous script. Ex: https://www.legal500.com/firms/17741-abello-ip-firm/23693-paris-france/) and returns available information of the firm such as logo, address, phone number, memberships, key clients, lawyers, among others. 

You can run the script by simply going to the directory where the script is saved and run 'python firm_details.py [url]'.
