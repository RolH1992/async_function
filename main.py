# main.py
import asyncio
from cli import menu  

async def main():
    await menu()

asyncio.run(main())
