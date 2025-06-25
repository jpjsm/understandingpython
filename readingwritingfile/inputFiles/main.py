import sys
import uvicorn
from app import app


def main() -> int:
    uvicorn.run(app=app, host="{{host}}", port={{port}})
    return 0


if __name__ == "__main__":
    sys.exit(main())
