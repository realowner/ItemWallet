from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from starlette import status

from app.core.dependencies import get_game_service
from app.schemas.extra.game import CreateUpdateGame, GetGame, DeleteGameResponse
from app.services.extra.game import GameService

game_router = APIRouter()


@game_router.post('/games', response_model=GetGame)
async def create_game(game: CreateUpdateGame, service: GameService = Depends(get_game_service)):
    game_object = await service.add_game(game)
    return game_object


@game_router.get('/games', response_model=list[GetGame])
async def get_all_games(service: GameService = Depends(get_game_service)):
    game_object = await service.get_all()
    return game_object


@game_router.get('/games/{game_id}', response_model=GetGame)
async def get_one_games(game_id: int, service: GameService = Depends(get_game_service)):
    game_object = await service.get_one(game_id)

    #TODO: подумать о перемещении в сервисы
    if not game_object:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Game with id {game_id} not found"
        )

    return game_object


@game_router.delete('/games/{game_id}', response_model=DeleteGameResponse)
async def delete_game(game_id: int, service: GameService = Depends(get_game_service)):
    game_object = await service.delete_game(game_id)

    # TODO: подумать о перемещении в сервисы
    if not game_object:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Game with id {game_id} not found"
        )

    return game_object


@game_router.patch('/games/{game_id}', response_model=GetGame)
async def update_game(game_id: int, game: CreateUpdateGame, service: GameService = Depends(get_game_service)):
    game_object = await service.update_game(game_id, game)

    # TODO: подумать о перемещении в сервисы
    if not game_object:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Game with id {game_id} not found"
        )

    return game_object
