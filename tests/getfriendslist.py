import steampy.ISteamUser as SteamUser
import steampy


print(SteamUser.GetFriendsList(steam_id=76561199208150262, api_key=steampy.get_api_key(), relationship="all"))