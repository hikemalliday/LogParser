import asyncio
import logparser

async def main():
    try:
        await logparser.start_parse()
    finally:
        print("main finally block")

if __name__ == "__main__":
    asyncio.run(main())
    