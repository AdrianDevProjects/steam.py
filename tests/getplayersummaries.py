import steampy.ISteamUser as SteamUser
import steampy



print(SteamUser.GetPlayerSummaries(steam_ids=[76561199208150262], api_key=steampy.get_api_key()))