from fastapi import APIRouter

product_router = APIRouter(prefix="/product")


@product_router.get('/')
async def product_list():
    return {
        "msg": "Product API"
    }

