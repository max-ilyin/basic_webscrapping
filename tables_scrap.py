import requests
from bs4 import BeautifulSoup
import pandas as pd

# url = "https://www.skysports.com/premier-league-table"


def get_league_table(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    tablelist = []
    league_table = soup.find("table", class_="standing-table__table")
    for team in league_table.find_all("tbody"):
        rows = team.find_all("tr")
        for row in rows:
            pl_team = row.find(
                "td", class_="standing-table__cell standing-table__cell--name"
            ).text.strip()
            pl_points = row.find_all("td", class_="standing-table__cell")[9].text
            # print(pl_team, pl_points)
            teamleague = {"name": pl_team, "points": pl_points}
            tablelist.append(teamleague)
    return tablelist


data = get_league_table("https://www.skysports.com/premier-league-table")

df = pd.DataFrame(data)
df.to_csv("leagetable.csv")
df.to_excel("leagetable.xlsx")
print("done")
