"""run multiple http requests"""

from turtle import back
import logsetup
import logging
import pathlib
import aiohttp
import asyncio
import json
import random
import multiprocessing

# define modulename from file
_modulename_ = pathlib.Path(__file__).stem

# creating module logger
module_logger = logging.getLogger(f"main.{_modulename_}")


async def intosyllynumbers(session: aiohttp.ClientSession):

    module_logger.info("Started.")
    _status = None
    _content = None
    _path = None
    _verb = None
    _body = None
    _path_params = None
    _qry_params = None

    _task = random.randint(1, 3)
    if _task == 1:
        _verb = "GET"
        _path = "/"
        async with session.get("/") as resp:
            _status = resp.status
            _content = await resp.text()

    elif _task == 2:
        _verb = "GET"
        _path = "/primes"
        async with session.get("/primes") as resp:
            _status = resp.status
            _content = await resp.text()

    elif _task == 4:
        n = random.randint(1, 10000000)
        _verb = "POST"
        _path = "/primes"
        _body = {"number": n}
        async with session.post("/primes", json={"number": n}) as resp:
            _status = resp.status
            _content = await resp.text()

    elif _task == 3:
        n = random.randint(1, 10000000)
        _verb = "GET"
        _path = "/primes/{p}"
        _path_params = n
        async with session.get(f"/primes/{n}") as resp:
            _status = resp.status
            _content = await resp.text()

    elif _task == 5:
        n = random.randint(1, 10000000)
        _verb = "DELETE"
        _path = "/primes/{p}"
        _path_params = n
        async with session.delete(f"/primes/{n}") as resp:
            _status = resp.status
            _content = await resp.text()

    elif _task == 6:
        n = random.randint(1, 10000000)
        _verb = "PUT"
        _path = "/primes/{p}"
        _path_params = n
        async with session.put(f"/primes/{n}", json={"number": n}) as resp:
            _status = resp.status
            _content = await resp.text()

    _info = {
        "verb": _verb,
        "path": _path,
        "body": _body,
        "path_params": _path_params,
        "query_params": _qry_params,
        "status": _status,
        "content": _content,
    }
    module_logger.info({json.dumps(_info)})
    module_logger.info("Terminated.")


async def main():
    module_logger.info("Started.")

    number_of_cpus = multiprocessing.cpu_count()

    max_calls = 1
    if number_of_cpus > 2:
        max_calls = (number_of_cpus - 2) * 2

    background_tasks = []
    for i in len(background_tasks):
        background_tasks[i] = set()

    async with aiohttp.ClientSession("http://localhost:20101") as session:
        for i in range(100000):
            background_group = 1 % max_calls

            while len(background_tasks[background_group]) > max_calls:
                await asyncio.sleep(0.5)
                print(f"   waited 1/2 secondfor group: {background_group}")

            print(f"Creating task in background group {background_group}...", end="")
            tsk = asyncio.create_task(intosyllynumbers(session))

            # Add task to the collection.
            # This creates a strong reference.
            background_tasks.add(tsk)

            # To prevent keeping references to finished tasks forever,
            # make each task remove its own reference from the set after
            # completion:
            tsk.add_done_callback(background_tasks.discard)
            await asyncio.sleep(0.005)
            print("done")

        while background_tasks:
            await asyncio.sleep(1.0)

        await session.close()

    module_logger.info("Terminated.")


if __name__ == "__main__":
    main_logger = logging.getLogger("main")
    main_logger.setLevel(logsetup.defaultloglevel)

    asyncio.run(main(), debug=True)  # asyncio.run(main())
    main_logger.error("Execution complete !!")
