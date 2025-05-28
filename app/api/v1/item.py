from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from starlette import status

from app.core.dependencies import get_item_service
from app.schemas.item import CreateItem, UpdateItem, GetItem, DeleteItemResponse
from app.services.item import ItemService

item_router = APIRouter()


@item_router.post('/items', response_model=GetItem)
async def create_item(item: CreateItem, service: ItemService = Depends(get_item_service)):
    item_object = await service.add_item(item)
    return item_object


@item_router.get('/items', response_model=list[GetItem])
async def get_all_items(service: ItemService = Depends(get_item_service)):
    item_object = await service.get_all()
    return item_object


@item_router.get('/items/{item_id}', response_model=GetItem)
async def get_one_item(item_id: int, service: ItemService = Depends(get_item_service)):
    item_object = await service.get_one(item_id)

    #TODO: подумать о перемещении в сервисы
    if not item_object:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item type with id {item_id} not found"
        )

    return item_object


@item_router.delete('/items/{item_id}', response_model=DeleteItemResponse)
async def delete_item(item_id: int, service: ItemService = Depends(get_item_service)):
    item_object = await service.delete_item(item_id)

    # TODO: подумать о перемещении в сервисы
    if not item_object:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Game with id {item_id} not found"
        )

    return item_object


@item_router.patch('/items/{item_id}', response_model=GetItem)
async def update_item(item_id: int, item: UpdateItem,
                           service: ItemService = Depends(get_item_service)):
    item_object = await service.update_item(item_id, item)

    # TODO: подумать о перемещении в сервисы
    if not item_object:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Game with id {item_id} not found"
        )

    return item_object
