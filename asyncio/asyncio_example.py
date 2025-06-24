"""learning asyncio"""

import logsetup
import logging
import pathlib
import asyncio
from num2words import num2words
import datetime

# define modulename from file
_modulename_ = pathlib.Path(__file__).stem

# creating module logger
module_logger = logging.getLogger(f"main.{_modulename_}")


async def logme(n: int):
    await asyncio.sleep(0.02)
    module_logger.info(f"{n} == {num2words(n)}")


async def app():
    module_logger.info("starting")
    background_tasks = set()

    for i in range(100000):
        tsk = asyncio.create_task(logme(i))

        # Add task to the collection.
        # This creates a strong reference.
        background_tasks.add(tsk)

        # To prevent keeping references to finished tasks forever,
        # make each task remove its own reference from the set after
        # completion:
        tsk.add_done_callback(background_tasks.discard)
        if (i % 1000) == 999:
            module_logger.info(f"progress: {i+1}")

    while background_tasks:
        await asyncio.sleep(1.0)

    module_logger.info("completed")


if __name__ == "__main__":
    main_logger = logging.getLogger("main")
    main_logger.setLevel(logsetup.defaultloglevel)

    asyncio.run(app(), debug=True)  # asyncio.run(main())
    main_logger.error("Execution complete !!")
