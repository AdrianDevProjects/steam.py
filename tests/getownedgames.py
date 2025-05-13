import steampy.IPlayerService as playerService
import steampy

print(playerService.GetOwnedGames(steam_id=76561199208150262,
                                  api_key=steampy.get_api_key(),
                                  include_appinfo=True,
                                  include_played_free_games=False))