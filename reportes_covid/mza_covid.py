#!/usr/bin/env python3
# Extracting all coronavirus reports from Mendoza, Argentina Government

from bs4 import BeautifulSoup
import requests
import time


base_url = "http://www.prensa.mendoza.gov.ar/coronavirus-comunicado-del-ministerio-de-salud-desarrollo-social-y-deportes-de-mendoza-"
print(f"This program will request and download 200 reports from this website \n{base_url}")
input("Press enter to continue\n")
for i in range(185, 205):
    url = base_url + str(i)
    response = requests.get(url)
    
    if response.status_code == 200:
        print(f"Status ok for URL n°{i}")
        
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        s = soup.find("div", class_="the_content")
        
        #Open file and save contents.
        file = open(f'reporte-{i}.txt', 'w')
        file.write(s.get_text())
        file.close()
        
    else:
        print(f"Error {response.status_code} for URL n°{i}")
