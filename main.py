import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_character(api_key, realm: str, name: str,  region: str = "eu"):
    try:
        response = requests.get(
            "https://raider.io/api/v1/characters/profile",
            params={
            "access_key": api_key,
            "region": f"{region}",
            "realm": f"{realm}",
            "name": f"{name}"
            },
            headers={
                "accept": "application/json"
            }
        )
        return response
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None
    
def guild_info_on_boss_manaforge(api_key, realm: str, guild: str, boss: str, region: str = "eu", difficulty: str = "mythic"):
    try:
        response = requests.get(
            "https://raider.io/api/v1/guilds/boss-kill",
            params={
            "access_key": api_key,
            "region": region,
            "realm": realm,
            "guild": guild,
            "raid": "manaforge-omega",
            "boss": boss,
            "difficulty": difficulty
            },
            headers={
            "accept": "application/json"
            }
        )
        print(f"Request URL: {response.url}")
        return response
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY not found in environment variables")
    
    # response = get_character(api_key, region="eu", realm="Stormscale", name="razzyyx")
    # print(response.json())
    response = guild_info_on_boss_manaforge(api_key, region="eu", realm="Draenor", guild="Social Debuff", boss="dimensius")
    print(response.json())