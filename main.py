import time

from pydantic import BaseModel
import uvicorn
import keyboard as kb
import asyncio
from fastapi import FastAPI


app = FastAPI()


class DataModel(BaseModel):
    morph: str


async def give(data):
    morph = data.morph.split('\n')
    for i in morph:
        kb.press_and_release("'")
        kb.press_and_release("backspace")
        await asyncio.sleep(0.5)
        kb.write(f"{i}", delay=0.03)
        kb.press_and_release('enter')
        await asyncio.sleep(0.5)


@app.post('/morph/get')
async def add(data: DataModel):
    await give(data)
    return {
        'status': 'ok'
    }


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=1314)
