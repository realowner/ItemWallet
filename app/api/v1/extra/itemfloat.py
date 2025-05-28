from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from starlette import status

from app.core.dependencies import get_itemfloat_service
from app.schemas.extra.itemfloat import CreateItemFloat, UpdateItemFloat, GetItemFloat, DeleteItemFloatResponse
from app.services.extra.itemfloat import ItemFloatService

float_router = APIRouter()


@float_router.post('/floats', response_model=GetItemFloat)
async def create_item_float(item_float: CreateItemFloat,
                            service: ItemFloatService = Depends(get_itemfloat_service)):
    float_object = await service.add_float(item_float)
    return float_object


@float_router.get('/floats', response_model=list[GetItemFloat])
async def get_all_item_floats(service: ItemFloatService = Depends(get_itemfloat_service)):
    float_object = await service.get_all()
    return float_object


@float_router.get('/floats/{float_id}', response_model=GetItemFloat)
async def get_one_item_float(float_id: int, service: ItemFloatService = Depends(get_itemfloat_service)):
    float_object = await service.get_one(float_id)

    #TODO: подумать о перемещении в сервисы
    if not float_object:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item type with id {float_id} not found"
        )

    return float_object


@float_router.delete('/floats/{float_id}', response_model=DeleteItemFloatResponse)
async def delete_item_float(float_id: int, service: ItemFloatService = Depends(get_itemfloat_service)):
    float_object = await service.delete_float(float_id)

    # TODO: подумать о перемещении в сервисы
    if not float_object:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Game with id {float_id} not found"
        )

    return float_object


@float_router.patch('/floats/{float_id}', response_model=GetItemFloat)
async def update_item_float(float_id: int, item_float: UpdateItemFloat,
                            service: ItemFloatService = Depends(get_itemfloat_service)):
    float_object = await service.update_float(float_id, item_float)

    # TODO: подумать о перемещении в сервисы
    if not float_object:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Game with id {float_id} not found"
        )

    return float_object
