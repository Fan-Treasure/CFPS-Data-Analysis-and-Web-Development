import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
import json


app = FastAPI()

# 前端页面url
origins = [
    "http://localhost",
    "http://localhost:8010",
    "http://82.156.173.187",
    "http://82.156.173.187:8010",
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

@app.get("/index")
async def index():
    with open("time.json", encoding="utf-8") as f:
        time = json.load(f)
    time = str(int(time) + 1)
    fb = open('time.json', 'w', encoding='utf-8')
    fb.write(json.dumps(time, ensure_ascii=False, indent=2))
    fb.close()
    return {"state": "success", "time": int(time)}


if __name__ == '__main__':
    uvicorn.run(app=app, host='10.0.24.2', port=8020)

