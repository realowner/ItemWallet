import uvicorn

from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError, HTTPException
from fastapi.routing import APIRouter

from app.api.v1.extra.game import game_router
from app.api.v1.extra.itemtype import item_type_router
from app.utils.exceptions import (custom_http_exception_handler,
                                  validation_exception_handler,
                                  generic_exception_handler)


app = FastAPI(title='ItemWallet')

main_app_router = APIRouter()

app.include_router(main_app_router)
app.include_router(game_router)
app.include_router(item_type_router)

app.add_exception_handler(HTTPException, custom_http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(Exception, generic_exception_handler)

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
