from bs4 import BeautifulSoup
from collections import defaultdict
from aliance import models

def ali_view_get_and_save(file):
    if file:
        html_decode = file.read().decode('utf-8')
        soup = BeautifulSoup(html_decode, "html.parser")

    # Aliance
        ali_name = soup.find(id="icontent").h1.string   # name of an aliance
        if ali_name:
            aliance_name = models.Aliance.objects.create(label=ali_name) # Aliance was created

    # Players in Aliance
        ali_table = soup.find("table", class_="vis_tbl")
        if ali_table:
            aliance = defaultdict(list) # for dictionary with list-value
            for player in ali_table.find_all("a", class_="pname"):
                player_name = player.string.split(" ")[-1] # fiding the name on the last position in the list player
                print(player_name)
                zeme = player.find_previous_sibling("a").string 
                aliance[player_name].append(zeme) # dictionary of an aliance -> hrac: [zeme1, zeme2]
                player_in_aliance = models.Hrac.objects.create(name=player_name, aliance=aliance_name) # new player in the aliance




def ali_table_get_and_save(file):
    pass