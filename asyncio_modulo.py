import asyncio

async def main():
    print ("Hello ...")
    await asyncio.sleep(1)
    print ("... Word!")
asyncio.run(main())