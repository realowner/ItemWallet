from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from starlette import status

from app.core.dependencies import get_itemtype_service
from app.schemas.extra.itemtype import CreateUpdateGetItemType, GetItemType, DeleteGetItemTypeResponse
from app.services.extra.itemtype import ItemTypeService

item_type_router = APIRouter()


@item_type_router.post('/types', response_model=GetItemType)
async def create_item_type(item_type: CreateUpdateGetItemType, service: ItemTypeService = Depends(get_itemtype_service)):
    type_object = await service.add_type(item_type)
    return type_object


@item_type_router.get('/types', response_model=list[GetItemType])
async def get_all_item_types(service: ItemTypeService = Depends(get_itemtype_service)):
    type_object = await service.get_all()
    return type_object


@item_type_router.get('/types/{type_id}', response_model=GetItemType)
async def get_one_item_type(type_id: int, service: ItemTypeService = Depends(get_itemtype_service)):
    type_object = await service.get_one(type_id)

    #TODO: подумать о перемещении в сервисы
    if not type_object:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item type with id {type_id} not found"
        )

    return type_object


@item_type_router.delete('/types/{type_id}', response_model=DeleteGetItemTypeResponse)
async def delete_item_type(type_id: int, service: ItemTypeService = Depends(get_itemtype_service)):
    type_object = await service.delete_type(type_id)

    # TODO: подумать о перемещении в сервисы
    if not type_object:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Game with id {type_id} not found"
        )

    return type_object


@item_type_router.patch('/types/{type_id}', response_model=GetItemType)
async def update_item_type(type_id: int, item_type: CreateUpdateGetItemType,
                      service: ItemTypeService = Depends(get_itemtype_service)):
    type_object = await service.update_type(type_id, item_type)

    # TODO: подумать о перемещении в сервисы
    if not type_object:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Game with id {type_id} not found"
        )

    return type_object
