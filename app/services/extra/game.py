from app.schemas.extra.game import CreateUpdateGame
from app.repositories.base import BaseRepository


class GameService:
    def __init__(self, game_repo: BaseRepository):
        self.game_repo = game_repo

    async def add_game(self, data: CreateUpdateGame):
        data_dict = data.model_dump()
        game = await self.game_repo.add_object(data_dict)
        return game

    async def get_all(self):
        games = await self.game_repo.get_all()
        return games

    async def get_one(self, game_id: int):
        game = await self.game_repo.get_one(game_id)
        return game

    async def delete_game(self, game_id: int):
        game = await self.game_repo.delete_object(game_id)
        return game

    async def update_game(self, game_id: int, data: CreateUpdateGame):
        data_dict = data.model_dump()
        game = await self.game_repo.update_object(game_id, data_dict)
        return game
