import time

from pydantic import BaseModel
import uvicorn
import pyautogui as pag
from fastapi import FastAPI


app = FastAPI()


class DataModel(BaseModel):
    morph: str


@app.post('/morph/get')
async def add(data: DataModel):
    morph = data.morph.split('\n')
    for i in morph:
        pag.write(f'/{i} \n')
    return {
        'status': 'ok'
    }


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=1314)
