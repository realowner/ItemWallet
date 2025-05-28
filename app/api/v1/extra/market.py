from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from starlette import status

from app.core.dependencies import get_market_service
from app.schemas.extra.market import CreateUpdateMarket, GetMarket, DeleteMarketResponse
from app.services.extra.market import MarketService

market_router = APIRouter()


@market_router.post('/markets', response_model=GetMarket)
async def create_market(market: CreateUpdateMarket, service: MarketService = Depends(get_market_service)):
    market_object = await service.add_market(market)
    return market_object


@market_router.get('/markets', response_model=list[GetMarket])
async def get_all_markets(service: MarketService = Depends(get_market_service)):
    market_object = await service.get_all()
    return market_object


@market_router.get('/markets/{market_id}', response_model=GetMarket)
async def get_one_market(market_id: int, service: MarketService = Depends(get_market_service)):
    market_object = await service.get_one(market_id)

    #TODO: подумать о перемещении в сервисы
    if not market_object:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item type with id {market_id} not found"
        )

    return market_object


@market_router.delete('/markets/{market_id}', response_model=DeleteMarketResponse)
async def delete_market(market_id: int, service: MarketService = Depends(get_market_service)):
    market_object = await service.delete_market(market_id)

    # TODO: подумать о перемещении в сервисы
    if not market_object:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Game with id {market_id} not found"
        )

    return market_object


@market_router.patch('/markets/{market_id}', response_model=GetMarket)
async def update_market(market_id: int, market: CreateUpdateMarket,
                        service: MarketService = Depends(get_market_service)):
    market_object = await service.update_market(market_id, market)

    # TODO: подумать о перемещении в сервисы
    if not market_object:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Game with id {market_id} not found"
        )

    return market_object
