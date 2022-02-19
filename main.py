# Celine Mangahas
# Bronco ID: 013038025

import pandas as pd
from bs4 import BeautifulSoup
import requests

base_url = "https://pokemondb.net/pokedex/all"

res = requests.get(base_url)

soup = BeautifulSoup(res.content, 'html.parser')
table = soup.find(id='pokedex')
df = pd.DataFrame(columns=['ENTRY NUMBER', 'NAME', 'TYPES', 'TOTAL RATING', 'HP',
                           'ATTACK', 'DEFENSE', 'SPECIAL ATTACK', 'SPECIAL DEFENSE', 'SPEED'])

for entry in table.find_all("tr")[1:]:
    poke_list = list(entry.find_all("td"))
    entry_number = poke_list[0].find("span", class_="infocard-cell-data").text
    entry_name = poke_list[1].find("a", class_="ent-name").text
    entry_types = poke_list[2].find_all("a", class_="type-icon")
    entry_type_arr = []
    for entry_type in entry_types:
        entry_type_arr.append(entry_type.text)
    entry_total = poke_list[3].text
    entry_hp = poke_list[4].text
    entry_attack = poke_list[5].text
    entry_defense = poke_list[6].text
    entry_special_attack = poke_list[7].text
    entry_special_defense = poke_list[8].text
    entry_speed = poke_list[9].text
    df = df.append(
        {'ENTRY NUMBER': entry_number, 'NAME': entry_name, 'TYPES': entry_type_arr, 'TOTAL RATING': entry_total,
         'HP': entry_hp, 'ATTACK': entry_attack, 'DEFENSE': entry_defense, 'SPECIAL ATTACK': entry_special_attack,
         'SPECIAL DEFENSE': entry_special_defense, 'SPEED': entry_speed}, ignore_index=True)

df.to_csv("pokedex.csv")
print(df)
