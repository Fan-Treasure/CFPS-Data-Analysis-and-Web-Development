from fastapi import APIRouter
import json

router = APIRouter()

@router.get("/index")
async def index():
    with open("data/visitor.json", encoding="utf-8") as f:
        time = json.load(f)
    time = str(int(time) + 1)
    fb = open('data/visitor.json', 'w', encoding='utf-8')
    fb.write(json.dumps(time, ensure_ascii=False, indent=2))
    fb.close()
    return {"state": "success", "time": int(time)}