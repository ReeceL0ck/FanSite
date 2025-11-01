import requests
import os
from dotenv import load_dotenv

from models import puuids, playerModel

load_dotenv()

API_KEY =  os.getenv("RIOT_API_KEY")
REGION  =  os.getenv("RIOT_REGION", "EUW1")




def get_summoner_rank(puuid, region=REGION):

    url = f"https://{region}.api.riotgames.com/lol/league/v4/entries/by-puuid/{puuid}"
    headers = {"X-Riot-Token": API_KEY}
    
    print(f"Fetching data from: {url}")
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status() 
        data = response.json()
        
        # Returns second entry if exists (data[1] in JS)
        return data[1] if len(data) > 1 else data[0] if data else None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching summoner rank: {e}")
        raise

def response_handler(response):
    print   (f"Raw response data: {response}")
    try:
        player = playerModel(
            queueType=response.get('queueType'),
            rank=response.get('tier') +' '+ response.get('rank'),
            win_rate=round((response.get('wins') / (response.get('wins')+ response.get('losses')) * 100),2),
            leaguePoints=response.get('leaguePoints')
        )
        return player
    except Exception as e:
        print(f"Error creating player model: {e}")

if __name__ == "__main__":
    rank_data = get_summoner_rank(puuid=puuids.LARRY_LONGSTRIDE.value)

    print(puuids.LARRY_LONGSTRIDE.name,response_handler(rank_data))

