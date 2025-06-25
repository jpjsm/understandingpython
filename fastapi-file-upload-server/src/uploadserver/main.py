"""Main function to run."""

import os
import sys

import uvicorn

from app import app


def main() -> int:
    """Entry function.

    :return: zero on sucecssful exit.
    """
    # default port is 8080 if APP_PORT is not defined
    app_port = os.environ.get("APP_PORT", 18181)
    uvicorn.run(app=app, host="0.0.0.0", port=int(app_port))
    return 0


if __name__ == "__main__":
    sys.exit(main())
