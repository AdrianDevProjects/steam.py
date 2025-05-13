import steampy.IPlayerService as playerService
import steampy


print(playerService.GetRecentlyPlayedGames(steam_id=76561199208150262,
                                            api_key=steampy.get_api_key(),
                                            count=3))