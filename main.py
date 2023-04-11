import streamlit as st
import requests
from bs4 import BeautifulSoup

num_of_subpages = 29

fav_channels = ["Polsat","Polsat News","TVN 24","TVN","BBC World News","Polsat Film","Polsat Seriale","Kino Polska","TVN Fabuła","TV Puls","PULS 2","Comedy Central","Paramount Channel HD","AXN","AXN Spin","AXN White","AXN Black","FOX Comedy","FOX","Red Carpet TV HD","Warner TV HD","Ale kino+","TVN 7","TVN Style","BBC Lifestyle","BBC First","BBC Brit","BBC Earth","HISTORY","ZOOM TV","STOPKLATKA","Travel Channel","Tele 5 HD","Active Family","Biznes 24","CNN","TLC","Discovery Science","Discovery Historia","Animal Planet HD","Travel Channel","Planete+","Adventure","Fokus TV","CBS Reality","DocuBox HD","Da Vinci","CBS Europa","Sundance TV","Eurosport 1","Deutsche Welle","TV 5 Monde Europe","France 24"]
fav_channels_numbers = ["5","322","6","7","343","481","498","70","107","8","25","10","11","22","477","479","480","94","95","162","486","482","9","106","109","110","111","382","109","26","27","104","119","163","323","347","355","377","391","381","383","384","385","386","392","397","398","491","494","565","814","817","818"]
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
        if i < (len(soup_current)-1):
            soup_next = (soup_current[i].find_next_sibling("li"))
            title_soup_next = (soup_next.div).find("span", {"class": "title"})
            hour_soup_next = (soup_next.div).find("span", {"class": "hour"})
            # print(soup_next)
        hour_soup = (soup_current[i].div).find("span", {"class": "hour"})
        title_soup = (soup_current[i].div).find("span", {"class": "title"})
        if(soup_channels[i].text.strip() in fav_channels):
            hour = hour_soup.text.strip()
            hour_next = hour_soup_next.text.strip()
            channel = soup_channels[i].text.strip()
            programme = title_soup.a.text.strip()
            programme_next = title_soup_next.a.text.strip()
            channel_number = str(fav_channels_numbers[len(fav_channels) - fav_channels[::-1].index(soup_channels[i].text.strip()) - 1])
            st.markdown(channel + " **[ " + channel_number + " ]** "+ hour + " " + programme + " | " + hour_next + " " + programme_next)
