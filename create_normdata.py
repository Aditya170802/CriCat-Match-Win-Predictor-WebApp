import requests
from bs4 import BeautifulSoup
import pandas as pd

class who_wins:
    teams = {"india":6, "england":1, "australia":2, "new zealand":5, "west indies":4, "south africa":3, "pakistan":7, "bangladesh":25, "sri lanka":8, "afghanistan":40, "zimbabwe":9}
    def scrape_batting_data(self, team, matchtype):
        url = f"https://www.espncricinfo.com/records/team/averages-batting/{team}-{self.teams.get(team)}/{matchtype}?current=2"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        table = soup.find('table', class_='ds-w-full')

        data = []
        headers = ["Name", "Matches", "Runs", "Bat Avg"]
        data.append(headers)

        rows = table.find_all("tr")[1:]  # Exclude the header row
        for row in rows:
            cols = row.find_all("td")
            player = cols[0].text.strip()
            matches_played = cols[2].text.strip()
            wickets_taken = cols[5].text.strip()
            bowling_average = cols[7].text.strip()
            data.append([player, matches_played, wickets_taken, bowling_average])

        return data


    def scrape_bowling_data(self, team, matchtype):
        url = f"https://www.espncricinfo.com/records/team/averages-bowling/{team}-{self.teams.get(team)}/{matchtype}?current=2"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        table = soup.find('table', class_='ds-w-full')

        data = []
        headers = ["Name", "Matches", "Wkts", "Bowl Avg"]
        data.append(headers)

        rows = table.find_all("tr")[1:]  # Exclude the header row
        for row in rows:
            cols = row.find_all("td")
            player = cols[0].text.strip()
            matches_played = cols[2].text.strip()
            wickets_taken = cols[7].text.strip()
            bowling_average = cols[10].text.strip()
            data.append([player, matches_played, wickets_taken, bowling_average])

        return data
    
    def createdataset(self, team1, team2, match):
        if match.lower() == "t20i": 
            match = "t20"
        matchtype = {"t20":"twenty20-internationals-3", "test":"test-matches-1", "odi":"one-day-internationals-2"}
        data_bowl_t1 = self.scrape_bowling_data(team1, matchtype.get(match))
        data_bat_t1 = self.scrape_batting_data(team1, matchtype.get(match))
        data_bowl_t2 = self.scrape_bowling_data(team2, matchtype.get(match))
        data_bat_t2 = self.scrape_batting_data(team2, matchtype.get(match))
        t1_d2 = pd.DataFrame(data_bowl_t1[1:], columns=data_bowl_t1[0])
        t1_d1 = pd.DataFrame(data_bat_t1[1:], columns=data_bat_t1[0])
        t2_d2 = pd.DataFrame(data_bowl_t2[1:], columns=data_bowl_t2[0])
        t2_d1 = pd.DataFrame(data_bat_t2[1:], columns=data_bat_t2[0])
        merged_df_t1 = pd.merge(t1_d1, t1_d2, on=["Name", "Matches"])
        merged_df_t1["Country"] = team1.capitalize()
        merged_df_t2 = pd.merge(t2_d1, t2_d2, on=["Name", "Matches"])
        merged_df_t2["Country"] = team2.capitalize()
        t1_name_list = merged_df_t1['Name'].tolist()
        t2_name_list = merged_df_t2['Name'].tolist()
        merged_df = pd.concat([merged_df_t1, merged_df_t2], axis=0)
            
        merged_df = merged_df.replace('-', 0)
        merged_df['Runs'] = merged_df['Runs'].astype(int)
        merged_df['Matches'] = merged_df['Matches'].astype(int)
        merged_df['Bat Avg'] = merged_df['Bat Avg'].astype(float)
        merged_df['Bowl Avg'] = merged_df['Bowl Avg'].astype(float)
        merged_df['Wkts'] = merged_df['Wkts'].astype(int)

        masterdata = merged_df
        masterdata = masterdata.set_index("Name", drop = False)
        def normcode(na):
            score = 0.0
            for i in ['Matches', 'Runs', 'Bat Avg', 'Wkts', 'Bowl Avg']:
                score += (masterdata.loc[na, i] - masterdata[i].mean())/masterdata[i].std()
            return score
        Normal_Scores=[]
        for i in masterdata['Name']:
                Normal_Scores.append(round(normcode(i), 3))
        masterdata['Normal_Scores'] = Normal_Scores
        masterdata
        masterdata.to_excel(r'C:\Users\Lenovo\OneDrive\Desktop\self\sem 3 study\DS Hackathon\masterdatafiles\norm_players.xlsx')
        # print("success")
        return t1_name_list, t2_name_list




