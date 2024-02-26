import pickle

from fastapi import FastAPI, Request

app = FastAPI(
    title="BookkeepingServiceInside",
)


@app.get("/BookkeepingServiceInside/v1")
async def calculate_tax_from_check(request: Request) -> int:
    data: dict = pickle.loads(await request.body())
    tax = int(sum(map(lambda x: x * 100, data.values())) * 0.87)

    return tax


@app.get("/v2")
async def calculate_tax_from_check(name: str = 'dar', age: int = 101) -> dict:
    print(name, age)
    return {"name": name, "age": age}
