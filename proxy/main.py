import os

import aiohttp as aiohttp
from fastapi import FastAPI, Request

app = FastAPI(
    title="BookkeepingService",
)

aiohttp_session = aiohttp.ClientSession()

PORT_BOOKKEEPING_REST = os.environ.get("PORT_BOOKKEEPING_REST")
url = f'http://bookkeeping_rest:{PORT_BOOKKEEPING_REST}/BookkeepingServiceInside/v1'


@app.get("/BookkeepingService/v1")
async def calculate_tax_from_check(request: Request) -> int:
    async with aiohttp_session.get(url, data=await request.body()) as resp:
        tax: str = await resp.text()

    return int(tax)