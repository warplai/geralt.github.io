from fastapi import APIRouter

router = APIRouter()

enterprise_data = {
  "name": "GERALT",
  "description": "Ведущий дистрибьютор Российской кондитерской продукции",
  "links": [
    {"url": "https://www.ozon.ru/seller/geralt-1966150/?miniapp=seller_1966150"},
    {"url": "https://www.wildberries.ru/seller/4265297"},
    {"url": "https://market.yandex.ru/business--geralt/145957248?generalContext=t%3DshopInShop%3Bi%3D1%3Bbi%3D145957248%3B&rs=eJwzEv7EKMDBKLDwEKsEg0bPUVaN1SdZATqhBgE%2C&searchContext=sins_ctx"},
    {"url": "https://t.me/your-company"},
    {"url": "mailto:contact@example.com"},
    {"url": "https://your-company.com"}
  ]
}
@router.get("/api/data")
async def get_data():
    return enterprise_data