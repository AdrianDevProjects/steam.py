import steampy.ISteamNews as SteamNews
import steampy


print(SteamNews.GetNewsForApp(app_id=440, api_key=steampy.get_api_key(), count=3, max_length=300))