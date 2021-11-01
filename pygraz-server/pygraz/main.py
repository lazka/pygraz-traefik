from fastapi import FastAPI
import httpx

app = FastAPI(docs_url="/")


@app.get("/events")
async def events():
    async with httpx.AsyncClient() as client:
        r = await client.get(
            'https://api.meetup.com/PyGRAZ/events', timeout=10.0)
        return r.json()


@app.get("/test")
async def test():
    return {"name": "test"}
