from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from starlette import status

from app.core.dependencies import get_account_service
from app.schemas.extra.gameaccount import CreateUpdateAccount, GetAccount, DeleteAccountResponse
from app.services.extra.gameaccount import AccountService

game_account_router = APIRouter()


@game_account_router.post('/accounts', response_model=GetAccount)
async def create_game_account(account: CreateUpdateAccount, service: AccountService = Depends(get_account_service)):
    account_object = await service.add_account(account)
    return account_object


@game_account_router.get('/accounts', response_model=list[GetAccount])
async def get_all_game_accounts(service: AccountService = Depends(get_account_service)):
    account_object = await service.get_all()
    return account_object


@game_account_router.get('/accounts/{account_id}', response_model=GetAccount)
async def get_one_game_account(account_id: int, service: AccountService = Depends(get_account_service)):
    account_object = await service.get_one(account_id)

    #TODO: подумать о перемещении в сервисы
    if not account_object:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item type with id {account_id} not found"
        )

    return account_object


@game_account_router.delete('/accounts/{account_id}', response_model=DeleteAccountResponse)
async def delete_game_account(account_id: int, service: AccountService = Depends(get_account_service)):
    account_object = await service.delete_account(account_id)

    # TODO: подумать о перемещении в сервисы
    if not account_object:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Game with id {account_id} not found"
        )

    return account_object


@game_account_router.patch('/accounts/{account_id}', response_model=GetAccount)
async def update_game_account(account_id: int, account: CreateUpdateAccount,
                      service: AccountService = Depends(get_account_service)):
    account_object = await service.update_account(account_id, account)

    # TODO: подумать о перемещении в сервисы
    if not account_object:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Game with id {account_id} not found"
        )

    return account_object
