"""Silly numbers web-service"""

# standard imports by pip
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

# Adding Kulshan
from kulshan.kmetrics.middleware import fastapi_metrics


from primes import primes
from num2words import num2words

app = FastAPI()
app.add_middleware(fastapi_metrics)


@app.get("/")
async def home():
    return {"msg": "Hello Silly Numbers"}


@app.get("/primes")
async def getprimes():
    return JSONResponse(
        status_code=200,
        content={"primes": primes.knownprimes[0:1000]},
    )


@app.post("/primes")
async def addprime(_request: Request):
    _obj = await _request.json()
    number = int(_obj.number)

    inserted, n, msg, factors = primes.tryaddprime(number)

    if inserted:
        return JSONResponse(
            status_code=201, content={"value": n, "message": "successfully added"}
        )
    else:
        return JSONResponse(
            status_code=400,
            content={"value": n, "message": msg, "factors": factors},
        )


@app.get("/primes/{p}")
async def getprime(p: int) -> str:
    p = int(p)
    if p < 0:
        p = -p

    if p in primes.primes_set:
        return JSONResponse(
            status_code=200,
            content={
                "prime": p,
                "name": num2words(p),
                "nombre": num2words(p, "es"),
                "名前": num2words(p, "ja"),
            },
        )
    else:
        return JSONResponse(
            status_code=404,
            content={
                "prime": p,
                "error": f"Not a prime number, factors:{primes.factors(p)}",
            },
        )


@app.delete("/primes/{p}")
async def deleteprime(p: int) -> str:
    p = int(p)
    if p < 0:
        p = -p

    if p in primes.primes_set:
        return JSONResponse(
            status_code=423,
            content={"prime": p, "msg": "The requested resource is locked"},
        )


@app.put("/primes/{p}")
async def updateprime(p: int, value: int) -> str:
    p = int(p)
    if p < 0:
        p = -p

    value = int(value)
    if value < 0:
        value = -value

    if p != value:
        return JSONResponse(
            status_code=409,
            content={
                "prime": p,
                "value": value,
                "msg": "Conflict between path and parameter",
            },
        )

    if primes.isprime(p):
        return JSONResponse(
            status_code=200,
            content={"prime": p, "msg": "updated"},
        )

    return JSONResponse(
        status_code=418,
        content={
            "number": p,
            "msg": "I'm a teapot, you quested to brew coffee with these beans:"
            + f" {primes.factors(p)}",
        },
    )
