import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from starlette.responses import JSONResponse
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from app.models.settings import Settings
from app.routers import auth, user, database, visualize, visitor

app = FastAPI()

# 前端页面url
origins = [
    "http://localhost",
    "http://localhost:8000",
    "*",
]

# 后台api允许跨域
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(user.router)
app.include_router(database.router)
app.include_router(visualize.router)
app.include_router(visitor.router)


@AuthJWT.load_config
def get_config():
    return Settings()

@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    return JSONResponse(
        status_code=200,
        content={"status": "failure", "reason": exc.message, "status_code": exc.status_code}
    )

@app.exception_handler(RequestValidationError)
async def http_exception_handler(request, exc):
    return JSONResponse({"status": "failure", "reason": exc.errors()}, status_code=200)


if __name__ == '__main__':
    uvicorn.run(app=app, host='服务器ip地址', port='端口号')