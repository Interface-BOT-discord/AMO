import time
import random

import keyboard as kb
import asyncio

time.sleep(2)

randoms = ['yes', 'no', 'ystrelki', 'man', 'lol', 'dev']
morph = ['morph me none', f'ntag me {random.choice(randoms)}']


async def give():
    for i in morph:
        kb.press_and_release("'")
        kb.press_and_release("backspace")
        await asyncio.sleep(0.5)
        kb.write(f"{i}", delay=0.03)
        kb.press_and_release('enter')
        await asyncio.sleep(0.5)


asyncio.run(give())