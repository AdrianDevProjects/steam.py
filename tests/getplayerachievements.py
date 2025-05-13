import steampy.ISteamUserStats as SteamUserStats
import steampy



print(SteamUserStats.GetPlayerAchievements(steam_id=76561199208150262,
                                           app_id=1903340,
                                            api_key=steampy.get_api_key(),
                                           language="en"))