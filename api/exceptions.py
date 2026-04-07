
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from domain.exceptions.base import DomainException



app = FastAPI()

@app.exception_handler(DomainException)
async def domain_exception_handler(request: Request, exc: DomainException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": str(exc.message)},
    )
