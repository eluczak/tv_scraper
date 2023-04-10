import streamlit as st
import requests
from bs4 import BeautifulSoup

num_of_subpages = 29

fav_channels = ["TVN 24","TVN","TV Puls","TVN 7","AXN","WP","Puls 2","STOPKLATKA","Kino TV","National Geographic","FOX Comedy","FOX","Travel Channel","TVN Style","TVN Fabuła","CANAL+ DOMO","HOME TV HD","TVN24 BiS","Animal Planet HD","BBC Earth","Planete+","Discovery Historia","Da Vinci","Ale kino+","Warner TV HD","AMC","CBS Europa"]
fav_channels_numbers = ["6","7","8","9","22","23","24","27","71","93","94","100","104","106","107","146","159","335","381","382","384","391","398","482","486","488","491"]
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
            hour = hour_soup.text.strip()
            channel = soup_channels[i].text.strip()
            programme = title_soup.a.text.strip()
            channel_number = str(fav_channels_numbers[len(fav_channels) - fav_channels[::-1].index(soup_channels[i].text.strip()) - 1])
            st.markdown(hour + " - " + channel + " **[ " + channel_number + " ]** " + programme)
