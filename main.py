# main.py
import asyncio
from cli import menu  # Corrected import statement

async def main():
    await menu()

asyncio.run(main())