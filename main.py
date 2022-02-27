import streamlit as st
import requests
from bs4 import BeautifulSoup

num_of_subpages = 29

fav_channels = ["Polsat","Polsat News","TVN 24","TVN","BBC World News","Polsat Film","Polsat Seriale","Kino Polska","TVN Fabuła","TV Puls","PULS 2","Comedy Central","Paramount Channel HD","AXN","AXN Spin","AXN White","AXN Black","FOX Comedy","FOX","Red Carpet TV HD","Warner TV HD","Ale kino+","TVN 7","TVN Style","BBC Lifestyle","BBC First","BBC Brit","BBC Earth","HISTORY","ZOOM TV","STOPKLATKA","Travel Channel","Tele 5 HD","Active Family","Biznes 24","CNN","TLC","Discovery Science","Discovery Historia","Animal Planet HD","Travel Channel","Planete+","Adventure","Fokus TV","CBS Reality","DocuBox HD","Da Vinci","CBS Europa","Sundance TV","Eurosport 1","Deutsche Welle","TV 5 Monde Europe","France 24"]

for j in range(1,num_of_subpages+1):

    # a whole subpage
    url = "https://programtv.onet.pl/?dzien=0&strona="+str(j)
    response = requests.get(url)
    soup = BeautifulSoup(response.content,"html.parser")

    # all channels from the subpage
    soup_channels = soup.find_all("span", {"class": ["tvName"]})

    # all current programmes and their start times from the subpage
    soup_current = soup.findAll("li",{"class":"current"})

    for i in range( len(soup_current) ):
        hour_soup = (soup_current[i].div).find("span", {"class": "hour"})
        title_soup = (soup_current[i].div).find("span", {"class": "title"})
        if(soup_channels[i].text.strip() in fav_channels):
            st.write(hour_soup.text.strip() + " " + soup_channels[i].text.strip() + " - " + title_soup.a.text.strip())

