from app.schemas.extra.gameaccount import CreateUpdateAccount
from app.repositories.base import BaseRepository


class AccountService:
    def __init__(self, account_repo: BaseRepository):
        self.account_repo = account_repo

    async def add_account(self, data: CreateUpdateAccount):
        data_dict = data.model_dump()
        account_object = await self.account_repo.add_object(data_dict)
        return account_object

    async def get_all(self):
        account_object = await self.account_repo.get_all()
        return account_object

    async def get_one(self, account_id: int):
        account_object = await self.account_repo.get_one(account_id)
        return account_object

    async def delete_account(self, account_id: int):
        account_object = await self.account_repo.delete_object(account_id)
        return account_object

    async def update_account(self, account_id: int, data: CreateUpdateAccount):
        data_dict = data.model_dump()
        account_object = await self.account_repo.update_object(account_id, data_dict)
        return account_object
