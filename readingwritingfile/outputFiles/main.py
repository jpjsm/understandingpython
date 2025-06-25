import sys
import uvicorn
from app import app


def main() -> int:
    uvicorn.run(app=app, host="127.0.0.1", port=19031)
    return 0


if __name__ == "__main__":
    sys.exit(main())
