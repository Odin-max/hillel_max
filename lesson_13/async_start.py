# async/await
import asyncio


async def foo():
    await asyncio.sleep(1)
    print("I'm foo")


async def bar():
    await asyncio.sleep(2)
    print("I'm bar")


# async def main():
#     # tasks = [foo(), bar()]
#     # results = await asyncio.gather(*tasks)


# if __name__ == "__main__":
#     asyncio.run(main())
